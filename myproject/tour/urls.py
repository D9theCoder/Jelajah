# myproject/tour/urls.py
from django.urls import path
from . import views

app_name = 'tour'

urlpatterns = [
    path('fatahillah/', views.fatahillah, name='fatahillah'),
    path('mandiri/', views.mandiri, name='mandiri'),
    path('bankindonesia/', views.bankindonesia, name='bankindonesia'),
    path('virtual_fatahillah/', views.virtual_fatahillah, name='virtual_fatahillah'),
    path('virtual_mandiri/', views.virtual_mandiri, name='virtual_mandiri'),
    path('virtual_bankindonesia/', views.virtual_bankindonesia, name='virtual_bankindonesia')
    # path('virtual_fatahillah/', views.virtual_fatahillah, name='virtual_fatahillah'),
    # Other URL patterns
]
