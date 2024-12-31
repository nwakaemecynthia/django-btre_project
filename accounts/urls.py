from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='signin'),
    path('register', views.register, name='signup'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]