from django.urls import path, include

from . import views

urlpatterns = [
     path('', views.home_view, name='home'),
     path('clients', views.clients, name='clients'),
     path('signals', views.signals, name='signals'),
     path('user_home', views.user_home, name='user_home'),
     path('add-client', views.add_client, name='add_client'),
     path('add_signal', views.add_signal, name='add_signal'),
     path('login', views.login_view, name='login'),
     path('logout', views.logout_view, name='logout'),
]