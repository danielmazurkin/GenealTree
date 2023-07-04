from django.db import models
from pdf_reports.enums import StatusReport
from users.models import User
from peoples.models import People
import json


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

    def forming_data_for_pdf_report(self):
        """Необходимый метод для того чтобы отправлять данные в rabbitMq."""

        pdf_report = {
            "id": self.people.pk,
            "name": self.people.first_name,
            "last_name": self.people.last_name,
            "surname": self.people.surname,
            "date_of_birth": str(self.people.date_of_birth),
            "is_live": self.people.is_live,
            "sex": self.people.sex
        }

        return json.dumps(pdf_report)

    def __str__(self):
        return f"Отчет о {self.people.first_name} {self.people.surname}"

    class Meta:
        verbose_name = 'PDF-отчет'
        verbose_name_plural = 'PDF-отчеты'
