from django.conf.urls import include, url
from . import views

app_name = 'login'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',    views.login,    name='login'),
    url(r'^about/$',  views.about,  name='about'),
    url(r'^display/$',  views.display,  name='display'),
    ]
