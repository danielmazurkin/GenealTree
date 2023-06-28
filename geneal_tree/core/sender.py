from django.conf import settings
import pika


class SenderToServiceBase:
    """Класс отправителя в очередь Rabbit MQ."""

    BROKER_HOST = settings.BROKER_URL
    QUEUE_NAME = None
    POOL_CONNECTION = []

    def __init__(self, priority):
        self.priority = priority
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(self.BROKER_HOST))
        self.channel = self.connection.channel()

    def __enter__(self):
        if settings.QUEUE_NAME and len(self.POOL_CONNECTION) <= settings.MAX_RABBIT_CONNECTION:
            self.POOL_CONNECTION.append(self.channel)
            self.channel.queue_declare(queue=self.QUEUE_NAME)

            return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def send_data(self):
        """Метод отправляет данные в очередь"""
        pass
