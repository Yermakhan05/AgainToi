from django.urls import path
from . import views

urlpatterns = [
    path('calendar/add-event/', views.add_event, name='add-event'),
    path('calendar/', views.view_calendar, name='view-calendar'),
]