from rest_framework import generics, views, status
from rest_framework.response import Response
from django.shortcuts import redirect
from django.contrib.auth import get_user_model, authenticate
# Email sending and auth requirements
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# dev tools
from colorama import Fore, Style

# local
from writers.serializers import CreateWriterSerializer, WriterSerializer
from writers.token import email_auth_token

def message(msg):
    print(Fore.MAGENTA, Style.BRIGHT, '\b\b[#]', Fore.RED, msg, Style.RESET_ALL)

class CreateWriterAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateWriterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.name = user.name.title()
            user.is_active = False
            user.save()
            message(user.username + ' created an account.')
            ##### Sending Email verification mail #####
            site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = email_auth_token.make_token(user)
            link = 'http://{}/api/writer/activate/{}/{}'.format(site.domain, uid, token)
            email_subject = 'Confirm your account'
            mail = render_to_string('admin/activateMail.html', {'link':link, 'user':user})
            to_email = user.email
            email = EmailMessage(email_subject, mail, from_email='Key Blogs', to=[to_email])
            email.content_subtype = 'html'
            email.send()
            message('Email send to ' + user.username)
            return Response(status=status.HTTP_201_CREATED)
        message(serializer.errors)
        return Response(data=serializer.errors, status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

class ActivateWriterAPI(views.APIView):
    def get(self, request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        try:
            uid = force_bytes(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            user = None
        if user is not None and email_auth_token.check_token(user, token):
            user.is_active = True
            message(user.username + ' activated their account.')
            user.save()
            link = 'https://keyblogs.web.app/writer/setup/{}'.format(user.username)
            #link = 'http://localhost:3000/penName/{}'.format(user.username)
            return redirect(link)
        message('Invalid email verification link recieved.')
        link = 'https://keyblogs.web.app/invalid'
        #link = 'http://localhost:3000/invalid'
        return redirect(link)

class SetupWriterAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        user = get_user_model().objects.get(pk=kwargs['pk'])
        try:
            check = get_user_model().objects.get(username=request.data.get('username'))
        except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            check = None
        if check is not None:
            return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION, data={'error': 'Pen Name already taken.'})
        user.username = request.data.get('username')
        user.save()
        return Response(status=status.HTTP_200_OK)

class ManageWriterAPI(generics.RetrieveUpdateAPIView):
    serializer_class = WriterSerializer
    queryset = get_user_model().objects.all()
    lookup_field = "username"

class DeleteWriterAPI(views.APIView):
    def post(self, request, *args, **kwargs):
        email = get_user_model().objects.get(username=kwargs['username']).email
        password = request.data.get('password', None)
        user = authenticate(email=email, password=password)
        if user is not None:
            message(user.username + ' deleted their account.')
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
