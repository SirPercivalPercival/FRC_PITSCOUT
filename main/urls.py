from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('pit-scout/', views.pit_scout, name='pit_scout'),
    path('manual/', views.serve_manual, name='serve_manual'),
]