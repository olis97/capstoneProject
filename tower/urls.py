# IMPORTS
from django.urls import path
from . import views

# APP NAME
app_name = 'tower'

urlpatterns = [
    path('tower_about/', views.tower_about, name='tower_about'),
    path('tower_contact/', views.tower_contact, name='tower_contact'),
    path('', views.tower_home, name='tower_home'),
    path('tower_services/', views.tower_services, name='tower_services')
]