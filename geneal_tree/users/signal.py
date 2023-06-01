from django.db.models.signals import pre_save
from django.dispatch import receiver
from users.models import AllowedUser


@receiver(pre_save, sender=AllowedUser)
def allowed_user_signal(sender, instance, **kwargs):
    """Сигнал используется для проверки есть ли такой зарегистрированный пользователь."""
    print("Сигнал сработал")