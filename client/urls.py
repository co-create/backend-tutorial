from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:device_id>/', views.getData, name='device'),
]