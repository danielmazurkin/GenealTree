from django.contrib import admin, messages
from users.models import AllowedUser
from django.contrib.auth.models import User
from users.exception import UserDoesNotExistException


@admin.register(AllowedUser)
class AllowedUserAdmin(admin.ModelAdmin):
    """Разрешенный пользователь."""
    fields = ('login_user', )

    def save_model(self, request, obj, form, change):
        """Переопределение сохранения модели для создания многопользовательского режима."""
        if user := User.objects.filter(username=obj.login_user).first():
            obj.user_linked = user
            obj.owner_user = request.user
            obj.save()
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, "Вы пытаетесь добавить пользователя, которого не существует.")

    def get_queryset(self, request):
        """Переопределяем метод чтобы администратору отображались только его данные."""
        qs = super().get_queryset(request)
        return qs.filter(owner_user=request.user)