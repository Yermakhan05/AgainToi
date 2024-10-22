from django.utils import timezone
from django.shortcuts import render, redirect

from company.forms import VenueProfileForm
from company.models import CompanyCalendar
from django.contrib.auth.forms import UserCreationForm
from user.models import UserProfile


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             UserProfile.objects.create(user=user)
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, '', {'form': form})
#
#
# def edit_company_profile(request):
#     profile = request.user.companyprofile
#     if request.method == 'POST':
#         form = VenueProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#     else:
#         form = VenueProfileForm(instance=profile)
#     return render(request, 'edit_profile.html', {'form': form})
#
#
#
#
# def view_calendar(request):
#     events = CompanyCalendar.objects.filter(venue=request.user.companyprofile).order_by('event_date')
#     return render(request, 'view_calendar.html', {'events': events})
