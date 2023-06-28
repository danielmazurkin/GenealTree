from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusReport(models.TextChoices):
    IN_PROGRESS = "in_progress", _("В процессе")
    COMPLETED = "JR", _("Завершено")

