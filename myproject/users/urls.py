from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_and_register, name='login'),
    path('register/', views.login_and_register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.update_profile, name='profile'),
]
