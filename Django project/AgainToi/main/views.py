from django.views.generic import ListView

from company.models import CompanyProfile
from main.models import SearchHistory, EventType
from show.models import ShowProfile

from django.contrib.auth.mixins import LoginRequiredMixin


class SearchPlacesView(ListView):
    model = CompanyProfile
    template_name = 'list/search_places.html'
    context_object_name = 'venues'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            if self.request.user.is_authenticated:
                SearchHistory.objects.create(user=self.request.user, search_query=query)
            return CompanyProfile.objects.filter(company_name__icontains=query)
        return CompanyProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class SearchShowsView(ListView):
    model = ShowProfile
    template_name = 'list/search_shows.html'
    context_object_name = 'shows'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            if self.request.user.is_authenticated:
                SearchHistory.objects.create(user=self.request.user, search_query=query)
            return ShowProfile.objects.filter(show_name__icontains=query)
        return ShowProfile.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class EventTypeListView(ListView):
    model = EventType
    template_name = 'list/event_types.html'
    context_object_name = 'event_types'
