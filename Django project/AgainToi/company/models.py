from django.db import models
from django.conf import settings
from user.models import UserOrder, Address


class CompanyProfile(models.Model):
    VENUE_TYPES = [
        ('restaurant', 'Restaurant'),
        ('cafe', 'Cafe'),
        ('hall', 'Hall'),
        ('club', 'Club'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL, null=True, blank=True)
    capacity = models.IntegerField()
    venue_type = models.CharField(max_length=50, choices=VENUE_TYPES)

    image = models.ImageField(upload_to='company/profile_images/', blank=True, null=True, default='profile_images/profile.jpeg')
    video = models.FileField(upload_to='company/videos/', blank=True, null=True)


class CompanyCalendar(models.Model):
    venue = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100)
    event_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)


class CompanyOrderAcceptance(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    venue = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(null=True, blank=True)

