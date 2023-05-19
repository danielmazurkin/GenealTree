# Generated by Django 4.1.4 on 2022-12-16 03:28

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('peoples', '0002_delete_biopeople'),
    ]

    operations = [
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