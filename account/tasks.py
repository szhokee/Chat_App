from celery import shared_task
from django.core.mail import send_mail
from decouple import config

@shared_task
def send_activation_code(email, code):
    send_mail(
        'Chat',
        f'http://localhost:8000/account/activate/{code}',
        config('EMAIL_HOST_USER'),
        [email]
    )

@shared_task
def send_reset_password_code(email, code):
    send_mail(
        'Chat',
        f'To reset your password use this code {code}',
        config('EMAIL_HOST_USER'),
        [email]
    )
