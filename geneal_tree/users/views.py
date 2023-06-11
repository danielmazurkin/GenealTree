from django.views import View
from django.template.response import TemplateResponse
from users.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect, reverse


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
            user.is_superuser = True
            user.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно.")

            admin_url = reverse('admin:index')
            return redirect(admin_url)

        messages.error(request, "Некорректная регистрация, произошли ошибки.")
        form = NewUserForm()

        return TemplateResponse(
            request,
            template='register.html',
            context={"register_form": form}
        )
