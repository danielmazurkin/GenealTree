from django.apps import AppConfig
from django.db.models.signals import pre_save


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = 'Пользователи'
    verbose_name_plural = 'Пользователи'

    def ready(self):
        from users.signal import allowed_user_signal
        pre_save.connect(allowed_user_signal)
