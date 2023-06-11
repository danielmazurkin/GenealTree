from django.db import models
from .enums import SexChoice
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User



class People(models.Model):
    """Модель которая описывает одного человека в генеалогическом дереве."""

    mother = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Мама человека',
        related_name='mother_access',
    )

    father = models.ForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Папа человека',
        related_name='father_access',
    )

    marriage = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='В браке',
        related_name='marriage_link',
        help_text='В этом поле вы указываете с кем человек состоит в браке. Можно оставить пустым если человек незамужем/не женат '
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20,
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=25
    )

    surname = models.CharField(
        verbose_name='Отчество',
        max_length=25,
        null=True,
        blank=True
    )

    date_of_birth = models.DateField(
        verbose_name='Дата рождения',
        null=True,
        blank=True
    )

    is_live = models.BooleanField(
        verbose_name='Жив',
        default=False,
        null=True,
    )

    sex = models.CharField(
        verbose_name='Пол',
        max_length=255,
        choices=SexChoice.choices,
    )

    owner_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def __str__(self):
        result = f'{self.last_name} {self.first_name}'

        if self.surname:
            result = f'{self.last_name} {self.first_name} {self.surname}'

        return result

    @property
    def pk_marriage(self):
        if getattr(self, 'marriage'):
            return self.marriage.pk

    @property
    def pk_mother(self):
        if getattr(self, 'mother'):
            return self.mother.pk

    @property
    def pk_father(self):
        if getattr(self, 'father'):
            return self.father.pk

    @property
    def avatar_url(self) -> str:
        if hasattr(self, 'avatarpeople'):
            url_form = (f'{settings.SITE_URL}{self.avatarpeople.photo_link.url}'
                        if hasattr(self.avatarpeople, 'photo_link') else None)
            return url_form

    @property
    def photos_link(self) -> list[str]:
        list_from_photo = []
        photos = self.photopeople_set.all()

        for photo in photos:
            list_from_photo.append(
                f'{settings.SITE_URL}{str(photo.photo_link.url)}'
            )

        return list_from_photo

    @property
    def bio_people(self) -> str:
        if hasattr(self, 'biopeople'):
            return mark_safe(self.biopeople)

    class Meta:
        unique_together = ('mother', 'father', )
        verbose_name = 'Человек (+ связь)'
        verbose_name_plural = 'Люди ( + связи)'
