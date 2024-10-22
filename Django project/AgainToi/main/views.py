from django.shortcuts import render
from company.models import CompanyProfile
from show.models import ShowProfile


def search_places(request):
    query = request.GET.get('q')
    venues = CompanyProfile.objects.filter(company_name__icontains=query) if query else CompanyProfile.objects.none()
    return render(request, 'search_places.html', {'venues': venues, 'query': query})


def search_shows(request):
    query = request.GET.get('q')
    shows = ShowProfile.objects.filter(show_name__icontains=query) if query else ShowProfile.objects.none()
    return render(request, 'search_shows.html', {'shows': shows, 'query': query})
