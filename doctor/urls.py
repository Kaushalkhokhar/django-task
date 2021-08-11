from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='doctor-login' ),
    path('register/', views.login, name='doctor-register' ),
    path('list/', views.login, name='doctor-list' ),
]