from django.db import models
from pdf_reports.enums import StatusReport
from users.models import User
from peoples.models import People


class TaskPDFReport(models.Model):
    """Модель с задачей для модели пользователя."""

    status = models.CharField(
        verbose_name='Статус задачи',
        max_length=255,
        choices=StatusReport.choices,
    )

    people = models.ForeignKey(
        People,
        verbose_name='Человек для отчетности.',
        on_delete=models.CASCADE,
        related_name='people_tasks'
    )

    owner_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    class Meta:
        verbose_name = 'PDF-отчет'
        verbose_name_plural = 'PDF-отчеты'
