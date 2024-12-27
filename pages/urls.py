from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('login', views.login, name='signin'),
    path('register', views.register, name='signup'),
    path('listings', views.listings, name='listings'),
]