from django.db.models.signals import pre_save
from django.dispatch import receiver
from users.models import AllowedUser
from django.conf import settings
import pika


@receiver(pre_save, sender=AllowedUser)
def allowed_user_signal(sender, instance, **kwargs):
    """Сигнал используется для проверки есть ли такой зарегистрированный пользователь."""
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=settings.BROKER_URL))
    channel = connection.channel()
    channel.queue_declare(queue='auth_queue')
    channel.basic_publish(exchange='',
                          routing_key='auth_queue',
                          body='Hello World!')
    connection.close()
