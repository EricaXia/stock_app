from django.urls import path
from stock_app import views

urlpatterns = [
    path('', views.stock_app, name='hello_world'),
]