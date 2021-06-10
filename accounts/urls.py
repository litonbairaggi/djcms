from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"), # name="products" use href
    path('customer/<str:pk>/', views.customer, name="customer"),
]