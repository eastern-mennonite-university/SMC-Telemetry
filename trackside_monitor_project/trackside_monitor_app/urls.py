from django.urls import path

from . import views

urlpatterns = [
    path('start-lora/', views.start_lora),
    path('stop-lora/', views.stop_lora),
    path('', views.index),
]
