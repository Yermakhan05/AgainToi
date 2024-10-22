from django.utils import timezone
from django.shortcuts import render, redirect

from company.forms import VenueProfileForm
from company.models import CompanyCalendar, CompanyProfile
from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def edit_company_profile(request):
    profile = request.user.companyprofile
    if request.method == 'POST':
        form = VenueProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('venue-dashboard')
    else:
        form = VenueProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})


def add_event(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        event_date = request.POST['event_date']
        description = request.POST.get('description', '')

        CompanyCalendar.objects.create(
            venue=request.user.companyprofile,
            event_name=event_name,
            event_date=timezone.make_aware(event_date),
            description=description
        )
        return redirect('venue-dashboard')
    return render(request, 'add_event.html')


def view_calendar(request):
    events = CompanyCalendar.objects.filter(venue=request.user.companyprofile).order_by('event_date')
    return render(request, 'view_calendar.html', {'events': events})
