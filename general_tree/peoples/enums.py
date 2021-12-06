from django.db import models
from django.utils.translation import gettext_lazy as _


class DegreeKinship(models.TextChoices):
    """TextChoices для степени родства."""

    SON = 'SON', _('Сын')
    DAUGHTER = 'DAUGHTER', _('Дочь')
    MATHER = 'MATHER', _('Мать')
    FATHER = 'FATHER', _('Отец')
    HUSBAND = 'HUSBAND', _('Муж')
    WIFE = 'WIFE', _('Жена')
