from django.urls import path
from .views import CompanyRegister, CompanyProfileView, Order
from . import views

urlpatterns = [
    path('order/accept/<int:order_id>/', views.accept_order, name='accept_order'),
    path('register/', CompanyRegister, name='venue_register'),
    path('profile/', CompanyProfileView, name='venue_profile'),
    path('order/', Order, name='order'),
]
