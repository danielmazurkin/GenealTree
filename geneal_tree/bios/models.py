from django.db import models
from peoples.models import People
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.html import format_html


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

    owner_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def __str__(self):
        return format_html(f'{self.text_bio[0:100]}')

    class Meta:
        verbose_name = 'Биография человека'
        verbose_name_plural = 'Биографии людей'
