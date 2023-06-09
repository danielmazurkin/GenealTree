from django.db import models
from django.contrib.auth.models import User



class AllowedUser(models.Model):
    """Список разрешенных пользователей для просмотра дерева."""

    login_user = models.CharField(
        max_length=50,
        verbose_name="Логин пользователя",
        null=True,
        blank=True,
    )

    user_linked = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='user_linked'
    )

    owner_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def __str__(self):
        return f'Разрешенный пользователь: {self.login_user}'

    class Meta:
        verbose_name = "Разрешенный пользователь"
        verbose_name_plural = "Разрешенные пользователи"


class FriendLinkedTree(models.Model):
    """Модель которая отражает ссылки на дружественные деревья, фотографии."""

    user = models.ForeignKey(
        User,
        verbose_name="Дружественный пользователь",
        on_delete=models.CASCADE,
    )

    user_linked = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_owners',
    )

    def __str__(self):
        return f"Ссылки пользователя {self.user}"

    class Meta:
        verbose_name = "Дружественный пользователь"
        verbose_name_plural = "Дружественные пользователи"
