# Generated by Django 4.2.2 on 2023-06-28 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('peoples', '0004_alter_people_owner_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskPDFReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('in_progress', 'В процессе'), ('JR', 'Завершено')], max_length=255, verbose_name='Статус задачи')),
                ('owner_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people_tasks', to='peoples.people', verbose_name='Человек для отчетности.')),
            ],
            options={
                'verbose_name': 'PDF-отчет',
                'verbose_name_plural': 'PDF-отчеты',
            },
        ),
    ]
