from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
RES = '''
<span>
<style>
@import url('https://fonts.googleapis.com/css2?family=Electrolize&family=Montserrat&display=swap');
</style>
<center style="color: tomato; font-size: 3vh; font-family: 'Electrolize', sans-serif;"><h2>KeyBlogs API</h2></center><br />
<div style="margin-left: 20vw; cursor: pointer; font-size: 2vh; font-family: 'Montserrat', sans-serif;">
    <p style="color: black; font-weight:900;">Admin : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/admin/</a></p>
    <br />
    <p style="color: black; font-weight:900;">Login Writer : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/writer/login/</a></p>
    <p style="color: black; font-weight:900;">Logout Writer : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/writer/logout/:pk/</a></p>
    <p style="color: black; font-weight:900;">Create Writer : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/writer/create/</a></p>
    <p style="color: black; font-weight:900;">Activate Writer : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/writer/activate/:uidb64/:token/</a></p>
    <p style="color: black; font-weight:900;">Setup Writer : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/writer/setup/:pk/</a></p>
    <p style="color: black; font-weight:900;">View and Update Writer : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/writer/manage/:username/</a></p>
    <p style="color: black; font-weight:900;">Delete Writer : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/writer/delete/:username/</a></p>
    <p style="color: black; font-weight:900;">Search Writer : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/writer/earch/</a></p>
    <p style="color: black; font-weight:900;">Follow Writer : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/writer/follow/:user_pk/:writer_pk/</a></p>
    <br />
    <p style="color: black; font-weight:900;">Blog Feed : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/blog/feed/</a></p>
    <p style="color: black; font-weight:900;">Create Blog : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/blog/create/</a></p>
    <p style="color: black; font-weight:900;">View, Update and Delete Blog : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/blog/manage/:pk/</a></p>
    <p style="color: black; font-weight:900;">Like Blog : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/blog/like/:writer_pk/:blog_pk/</a></p>
    <p style="color: black; font-weight:900;">Save Blog : <a style="color: rgb(0, 128, 255); font-weight:500; ">http:keyblogsapi.herokuapp.com/api/blog/save/:writer_pk/:blog_pk/</a></p>
</div></span>
'''

def index(request):
    return HttpResponse(RES)

urlpatterns = [
    path('', index, name="index"),
    path('api/', index, name="api"),
    path('admin/', admin.site.urls),
    path('api/writer/', include('writers.urls')),
    path('api/blog/', include('blogs.urls')),
]
