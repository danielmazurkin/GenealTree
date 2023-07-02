from core.sender import SenderToServiceBase
import pika


class SenderToServicePDF(SenderToServiceBase):
    """Отправка в Rabbit MQ данных."""

    QUEUE_NAME = 'pdf_forming'

    def send_data(self, body):
        self.channel.basic_publish(exchange='',
                                   routing_key=self.QUEUE_NAME,
                                   body=body)