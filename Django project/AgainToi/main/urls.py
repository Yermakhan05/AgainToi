from django.urls import path
from .views import SearchPlacesView, SearchShowsView, EventTypeListView


urlpatterns = [
    path('search/places/', SearchPlacesView.as_view(), name='search_places'),
    path('search/shows/', SearchShowsView.as_view(), name='search_shows'),
    path('event-types/', EventTypeListView.as_view(), name='event_types'),
]