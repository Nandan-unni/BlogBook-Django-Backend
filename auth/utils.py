# from django.conf import settings
from writers.views import message
import smtplib
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from rest_framework import status


def send_email(data, user, type):
    data["email_data"]["user_name"] = user.name
    data["email_data"]["user_email"] = user.email
    email = EmailMessage(
        data["email_subject"],
        render_to_string(data["email_file"], data["email_data"]),
        from_email="BlogBook",
        to=[user.email],
    )
    email.content_subtype = "html"
    try:
        email.send()
    except (smtplib.SMTPAuthenticationError, smtplib.SMTPConnectError) as error:
        message(
            f"{type} mail sending failed for {user.name} ({user.pk}) due to {str(error)}."
        )
        return status.HTTP_204_NO_CONTENT
    message(f"{type} mail send to {user.name} ({user.pk})")
    return status.HTTP_201_CREATED
