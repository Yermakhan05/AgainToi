from django.urls import path
from .views import CompanyRegister, CompanyProfileView, Order

urlpatterns = [
    path('register/', CompanyRegister, name='venue_register'),
    path('profile/', CompanyProfileView, name='venue_profile'),
    path('order/', Order, name='order'),
]
