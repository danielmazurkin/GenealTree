from django.db import models


class AllowedUser(models.Model):
    """Список разрешенных пользователей для просмотра дерева."""

    login_user = models.CharField(
        max_length=50,
        verbose_name="Логин пользователя",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Разрешенный пользователь: {self.login_user}'

    class Meta:
        verbose_name = "Разрешенный пользователь"
        verbose_name_plural = "Разрешенные пользователи"
