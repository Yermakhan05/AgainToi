from django.db import models
from django.contrib.auth.models import User
from users.models import UserOrder


class CompanyProfile(models.Model):
    VENUE_TYPES = [
        ('restaurant', 'Restaurant'),
        ('cafe', 'Cafe'),
        ('hall', 'Hall'),
        ('club', 'Club'),
        ('other', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    capacity = models.IntegerField()
    venue_type = models.CharField(max_length=50, choices=VENUE_TYPES)


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

