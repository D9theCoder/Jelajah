from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_and_register, name='login'),
    path('register/', views.login_and_register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.update_profile, name='profile'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password/<str:uidb64>/<str:token>/', views.reset_password, name='reset_password')
]
