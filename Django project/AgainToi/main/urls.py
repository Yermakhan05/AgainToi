from django.urls import path
from .views import search_places, search_shows

urlpatterns = [
    path('search/places/', search_places, name='search_places'),
    path('search/shows/', search_shows, name='search_shows'),
]