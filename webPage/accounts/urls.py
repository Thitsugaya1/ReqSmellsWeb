from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('addreq/', views.addreq),
    path('products/', views.products),
    path('customer/', views.customer),
]