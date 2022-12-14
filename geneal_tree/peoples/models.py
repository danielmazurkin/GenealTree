from django.db import models
from .enums import SexChoice
from ckeditor.fields import RichTextField


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

    def __str__(self):
        result = f'{self.last_name} {self.first_name}'

        if self.surname:
            result = f'{self.last_name} {self.first_name} {self.surname}'

        return result

    class Meta:
        unique_together = ('mother', 'father', )
        verbose_name = 'Человек (+ связь)'
        verbose_name_plural = 'Люди ( + связи)'


class BioPeople(models.Model):
    """Модель которая описывает биографию человека."""

    people = models.OneToOneField(
        People,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Человек',
    )

    text_bio = RichTextField(
        verbose_name='Биография'
    )

    def __str__(self):
        return f'{self.text_bio[0:100]}'

    class Meta:
        verbose_name = 'Биография человека'
        verbose_name_plural = 'Биографии людей'
