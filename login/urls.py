from django.conf.urls import include, url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^addcomment/$', views.addcomment, name='addcomment'),
    # url(r'^success/$', views.success, name='success'),
    # url(r'^error/$', views.error, name='error'),
    # url(r'^successlogin/$', views.login_success, name='loginok'),
    # url(r'^errorlogin/$', views.login_error, name='loginerror'),
    ]
