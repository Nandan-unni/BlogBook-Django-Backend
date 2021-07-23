from rest_framework import views, status
from rest_framework.response import Response

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.conf import settings

import smtplib

from writers.serializers import WriterSerializer, SignupSerializer
from writers.token import email_auth_token
from writers.views import message


class SignUpView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.name = user.name.title()
            user.is_active = False
            user.save()
            message(f"{user.name} ({user.pk}) created an account.")

            ##### Sending Email verification mail #####
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = email_auth_token.make_token(user)
            link = f"{settings.API_URL}/auth/verifyemail/{uid}/{token}/"
            print(link)
            email_subject = "Confirm your account"
            mail = render_to_string("activateMail.html", {"link": link, "user": user})
            to_email = user.email
            email = EmailMessage(
                email_subject, mail, from_email="Key Blogs", to=[to_email]
            )
            email.content_subtype = "html"
            try:
                email.send()
                message(f"Auth Email send to {user.name} ({user.pk})")
            except smtplib.SMTPAuthenticationError:
                user.is_active = True
                user.save()
                message(f"Auth Email sending failed for {user.name} ({user.pk})")
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(status=status.HTTP_201_CREATED)
        message(serializer.errors)
        return Response(
            data=serializer.errors, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
        )


class SignInView(views.APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        user = authenticate(
            username=data.get("email", None), password=data.get("password", None)
        )
        print(data)
        if user is not None:
            login(request, user)
            message(f"{user.name} ({user.pk}) logged in.")
            serializer = WriterSerializer(user)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        message("User not found.")
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


class SignOutView(views.APIView):
    def get(self, request, **kwargs):
        user = get_user_model().objects.get(pk=kwargs["pk"])
        message(f"{user.name} ({user.pk}) logged out. ")
        logout(request)
        return Response(status=status.HTTP_200_OK)


class VerifyEmailView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            uid = force_bytes(urlsafe_base64_decode(kwargs["uidb64"]))
            print(int.from_bytes(urlsafe_base64_decode(kwargs["uidb64"])))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            user = None
        if user is not None and email_auth_token.check_token(user, kwargs["token"]):
            user.is_active = True
            message(f"{user.name} ({user.pk}) activated their account.")
            user.save()
            link = f"{settings.CLIENT_URL}/emailverify/success/{user.pk}/"
            return redirect(link)
        message("Invalid email verification link recieved.")
        link = f"{settings.CLIENT_URL}/emailverify/error/"
        return redirect(link)
