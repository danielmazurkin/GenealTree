# Generated by Django 4.2.2 on 2023-06-09 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_alloweduser_owner_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='alloweduser',
            name='user_linked',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_linked', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
