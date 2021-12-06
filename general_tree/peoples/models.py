from django.db import models
from .enums import DegreeKinship
from mptt.models import MPTTModel, TreeForeignKey


class People(MPTTModel):
    """Модель которая описывает одного человека в генеалогическом дереве."""

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родитель этого человека'
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

    def __str__(self):
        if not self.surname:
            return f'{self.last_name} {self.first_name}'
        else:
            return f'{self.last_name} {self.first_name} {self.surname}'

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'


class PhotoPeople(models.Model):
    """Модель которая описывает фотографии людей."""

    photo_link = models.ImageField(
        verbose_name='Изображение',
        upload_to='images_peoples/'
    )

    people = models.ForeignKey(
        People,
        verbose_name='Человек',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"Фотография для человека {self.people}"

    class Meta:
        verbose_name = 'Фотография человека'
        verbose_name_plural = 'Фотографии людей'


class BioPeople(models.Model):
    """Модель которая описывает биографию человека."""

    people = models.ForeignKey(
        People,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Человек',
    )

    text_bio = models.TextField(
        verbose_name='Биография'
    )

    class Meta:
        verbose_name = 'Биография человека'
        verbose_name_plural = 'Биографии людей'


class RelativePeople(models.Model):
    """Модель родственника."""

    parent = models.ForeignKey(
        People,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Для кого родственник'
    )

    degree_of_kinship = models.CharField(
        max_length=50,
        choices=DegreeKinship.choices,
        verbose_name='Степень родства'
    )

    class Meta:
        verbose_name = 'Родственник'
        verbose_name_plural = 'Родственники'
