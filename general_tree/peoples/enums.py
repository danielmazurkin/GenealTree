from django.db import models
from django.utils.translation import gettext_lazy as _


class SexChoice(models.TextChoices):
    """TextChoices на пол."""

    MALE = 'MALE', _('Мужской')
    FEMALE = 'FEMALE', _('Женский')
    NOT_UNDEFINED = 'NOT_UNDEFINED', _('Не определен')
