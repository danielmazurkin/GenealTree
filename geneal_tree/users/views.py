from django.views import View
from django.template.response import TemplateResponse
from users.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect
from users.tasks import send_mail_func
from django.contrib.auth import get_user_model
from common.generate_token import account_activation_token


class UserView(View):
    """Вью для работы с пользователями."""

    def get(self, request):
        """Возвращает страницу с регистрацией."""
        form = NewUserForm(request.POST)
        return TemplateResponse(
            request,
            template='register.html',
            context={"register_form": form}
        )

    def post(self, request):
        """Регистрирует пользователя, сразу делая его администратором."""
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_active = False
            user.is_superuser = True
            user.save()
            login(request, user)

            send_mail_func.delay(user.email, user.pk, account_activation_token.make_token(user))
            admin_url = reverse('admin:index')
            return redirect(admin_url)

        messages.error(request, "Некорректная регистрация, произошли ошибки.")
        form = NewUserForm()

        return TemplateResponse(
            request,
            template='register.html',
            context={"register_form": form}
        )


def activate(request, uidb64, token):
    """Типовое подтверждение email почты."""
    User = get_user_model()

    try:
        user = User.objects.get(pk=int(uidb64))
    except User.DoesNotExist:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Спасибо за подтверждение email.')
    else:
        messages.error(request, 'Ссылка активации не валидная.')

    return HttpResponseRedirect("/admin/")

