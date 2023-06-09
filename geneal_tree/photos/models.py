from django.db import models
from peoples.models import People
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class PhotoPeople(models.Model):
    """Модель которая описывает фотографии людей."""

    photo_link = models.ImageField(
        verbose_name='Изображение',
        upload_to='images_peoples/',
    )

    people = models.ForeignKey(
        People,
        verbose_name='Человек',
        on_delete=models.SET_NULL,
        null=True
    )

    description = RichTextField(
        verbose_name='Описание фотографии',
        null=True,
        blank=True,
    )

    owner_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def __str__(self):
        result_without_people = 'Фотография для человека'
        result_with_people = f"Фотография для человека {self.people}"
        str_result = result_with_people if hasattr(self, 'people') else result_without_people
        return str_result

    class Meta:
        verbose_name = 'Фотография человека'
        verbose_name_plural = 'Фотографии людей'


class AvatarPeople(models.Model):

    photo_link = models.ImageField(
        verbose_name='Аватар человек',
        upload_to='images_peoples/',
    )

    people = models.OneToOneField(
        People,
        verbose_name='Человек',
        on_delete=models.SET_NULL,
        null=True,
    )

    owner_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )

    def __str__(self):
        result = ''

        if hasattr(self.people, 'first_name'):
            result = f'Аватар для человек {str(self.people)}'

        return result

    class Meta:
        verbose_name = 'Аватар для профиля'
        verbose_name_plural = 'Аватарки для профилей'