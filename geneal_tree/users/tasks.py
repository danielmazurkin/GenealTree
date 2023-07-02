from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True)
def send_mail_func(self, email_to_send, user_pk, token):
    """Задача отправляет сообщение с подтверждением регистрации на почту."""

    mail_subject="Подтверждение регистрации в генеалогическом дереве"
    message = f"Подтвердите аккаунт по ссылке: {settings.SITE_URL}/users/activate/{user_pk}/{token}"

    send_mail(
            subject= mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_to_send],
            fail_silently=True,
    )
