from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User

@shared_task
def send_message_task(sender_id, receiver_id, subject, message):
    sender = User.objects.get(id=sender_id)
    receiver = User.objects.get(id=receiver_id)
    email_subject = f"New message from {sender.username}: {subject}"
    email_body = f"You received a new message:\n\n{message}\n\nFrom: {sender.username}"
    send_mail(email_subject, email_body, sender.email, [receiver.email])
    return f"Email sent from {sender.username} to {receiver.username}"
