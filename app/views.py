from django.contrib.auth import (get_user_model,
                                 authenticate,
                                 login as signin,
                                 logout as signout)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.core.mail import EmailMessage
from django.views import generic
from colorama import Fore, Style
from datetime import date

from .forms import (CreateAccountForm,
                    CreatePenNameForm,
                    EditAccountForm,
                    EditDPForm,
                    BlogCreationForm)
from .token import email_auth_token
from .models import Blog



def handler404(request, *args, **argv):
    response = TemplateResponse(request, 'app/404.html', {})
    response.status_code = 404
    return response

def message(msg):
    print(Fore.MAGENTA, Style.BRIGHT, '\b\b[#]', Fore.RED, msg, Style.RESET_ALL)




def index(request):
    if request.user.is_authenticated:
        return redirect('/blogs/view/')
    return render(request, 'app/index.html')

def logout(request):
    message(request.user.name + ' logged out.')
    signout(request)
    return redirect('/')

def login(request):
    err = {}
    #msg = 'Check your mail box and verify your mail id to continue'
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            signin(request, user)
            message(user.name + ' logged in.')
            if user.username == user.email:
                link = '/accounts/username/{}'.format(user.pk)
                return redirect(link)
            return redirect('/blogs/view/')
        err['err'] = 'Incorrect email or password. Make sure your email is verified.'
        message('User not found.')
        if not email and not password:
            err['err'] = 'Provide a email and password to login'
        elif not email:
            err['err'] = 'Provide a email to login'
        elif not password:
            err['err'] = 'Incorrect password'
    return render(request, 'registration/login.html', err)


class CreateAccountView(generic.View):
    def post(self, request):
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.name = user.name.capitalize()
            user.username = user.email
            user.is_active = False
            user.save()
            message(user.name + ' created an account.')
            ##### Sending Email verification mail #####
            site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = email_auth_token.make_token(user)
            link = 'http://{}/accounts/activate/{}/{}'.format(site.domain, uid, token)
            email_subject = 'Confirm your account'
            mail = render_to_string('registration/confirm_mail.html', {'link':link, 'user':user})
            to_email = user.email
            email = EmailMessage(email_subject, mail, from_email='Key Blogs', to=[to_email])
            email.content_subtype = 'html'
            email.send()
            message('Email send to ' + user.name)
            ##########################################
            return render(request, 'registration/confirm_to_msg.html')
        message('Error in creating account')
        return render(request, 'registration/create_account.html', {'form':form})
    def get(self, request):
        form = CreateAccountForm()
        return render(request, 'registration/create_account.html', {'form':form})


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None
    if user is not None and email_auth_token.check_token(user, token):
        user.is_active = True
        message(user.name + ' activated their account.')
        user.save()
        link = '/accounts/username/{}'.format(user.pk)
        return redirect(link)
    else:
        message('Invalid email verification link recieved.')
        return render(request, 'registration/confirm_failed.html')


class CreatePenNameView(generic.UpdateView):
    template_name = 'registration/create_username.html'
    form_class = CreatePenNameForm
    queryset = get_user_model().objects.all()
    success_url = '/blogs/view/'


class AccountView(generic.DetailView):
    template_name = 'registration/view_account.html'
    queryset = get_user_model().objects.all()
    context_object_name = 'blogger'
    def get_slug_field(self):
        return 'username'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel'] = self.kwargs['panel']
        return context

class EditAccountView(generic.UpdateView):
    template_name = 'registration/edit_account.html'
    form_class = EditAccountForm
    queryset = get_user_model().objects.all()
    context_object_name = 'user'
    def get_slug_field(self):
        return 'username'
    def get_success_url(self):
        return '/accounts/{}/blogs'.format(self.request.user.username)


class EditDPView(generic.UpdateView):
    template_name = 'registration/edit_dp.html'
    form_class = EditDPForm
    queryset = get_user_model().objects.all()
    context_object_name = 'user'
    def get_slug_field(self):
        return 'username'
    def get_success_url(self):
        return '/accounts/{}/blogs'.format(self.request.user.username)


@login_required
def delete_account(request):
    msg = {'title': 'Delete Account'}
    if request.method == 'POST':
        email = request.user.email
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            try:
                message(request.user.name + ' deleted their account.')
                get_user_model().objects.get(pk=request.user.id).delete()
                user = None
                return redirect('/')
            except get_user_model().DoesNotExist:
                message('User not found')
                msg['err'] = 'User not found.'
        else:
            message('Incorrect password for account deletion')
            msg['err'] = 'Incorrect Password'
    return render(request, 'registration/delete_account.html', msg)



class CreateBlogView(generic.CreateView):
    form_class = BlogCreationForm
    template_name = 'app/create_blog.html'
    success_url = '/blogs/view/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogsView(generic.ListView):
    template_name = 'app/view_blogs.html'
    queryset = Blog.objects.order_by('-pub_time')
    context_object_name = 'blogs'


class BlogView(generic.DetailView):
    queryset = Blog.objects.all()
    context_object_name = 'blog'
    template_name = 'app/view_blog.html'


class EditBlogView(generic.UpdateView):
    form_class = BlogCreationForm
    queryset = Blog.objects.all()
    context_object_name = 'blog'
    template_name = 'app/edit_blog.html'
    def get_success_url(self):
        return '/blogs/{}'.format(self.object.id)


class DeleteBlogView(generic.DeleteView):
    queryset = Blog.objects.all()
    context_object_name = 'blog'
    template_name = 'app/delete_blog.html'
    def get_success_url(self):
        return '/accounts/{}/blogs'.format(self.request.user.username)


@login_required
def like_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.user in blog.likes.all():
        blog.likes.remove(request.user)
        message(request.user.name + " unliked the blog '{}'".format(blog.title))
    else:
        blog.likes.add(request.user)
        message(request.user.name + " liked the blog '{}'".format(blog.title))
    return redirect('/blogs/view/')


@login_required
def follow(request, username):
    blogger = get_user_model().objects.get(username=username)
    user = request.user
    if user in blogger.followers.all():
        blogger.followers.remove(user)
        user.following.remove(blogger)
        message(user.name + ' unfollowed ' + blogger.name)
    else:
        blogger.followers.add(user)
        user.following.add(blogger)
        message(user.name + ' followed ' + blogger.name)
    link = '/accounts/{}/following'.format(username)
    return redirect(link)
