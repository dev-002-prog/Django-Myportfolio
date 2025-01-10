from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='home'),
    path('intro.html', views.intro,name='intro'),
    path('service.html', views.service,name='service'),
    path('media.html', views.media,name='media'),
    path('wcontact.html', views.contact,name='contact'),
]
