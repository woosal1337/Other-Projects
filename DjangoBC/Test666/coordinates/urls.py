from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('products/', views.products),
    path('customer/', views.customer)
]
