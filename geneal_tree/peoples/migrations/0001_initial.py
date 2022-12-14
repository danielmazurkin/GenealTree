# Generated by Django 4.1.4 on 2022-12-14 13:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('surname', models.CharField(blank=True, max_length=25, null=True, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('is_live', models.BooleanField(default=False, null=True, verbose_name='Жив')),
                ('sex', models.CharField(choices=[('MALE', 'Мужской'), ('FEMALE', 'Женский')], max_length=255, verbose_name='Пол')),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='father_access', to='peoples.people', verbose_name='Папа человека')),
                ('marriage', models.ForeignKey(blank=True, help_text='В этом поле вы указываете с кем человек состоит в браке. Можно оставить пустым если человек незамужем/не женат ', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marriage_link', to='peoples.people', verbose_name='В браке')),
                ('mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mother_access', to='peoples.people', verbose_name='Мама человека')),
            ],
            options={
                'verbose_name': 'Человек (+ связь)',
                'verbose_name_plural': 'Люди ( + связи)',
                'unique_together': {('mother', 'father')},
            },
        ),
        migrations.CreateModel(
            name='BioPeople',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_bio', ckeditor.fields.RichTextField(verbose_name='Биография')),
                ('people', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='peoples.people', verbose_name='Человек')),
            ],
            options={
                'verbose_name': 'Биография человека',
                'verbose_name_plural': 'Биографии людей',
            },
        ),
    ]
