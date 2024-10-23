from django.db import models

from django.db import models
from django.contrib.auth.models import User
from users.models import UserOrder


class Host(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Photographer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class CameraOperator(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Dancer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Singer(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class ShowProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    show_name = models.CharField(max_length=100)
    host = models.ForeignKey(Host, on_delete=models.SET_NULL, null=True, blank=True)
    photographer = models.ForeignKey(Photographer, on_delete=models.SET_NULL, null=True, blank=True)
    camera_operator = models.ForeignKey(CameraOperator, on_delete=models.SET_NULL, null=True, blank=True)
    dancer = models.ForeignKey(Dancer, on_delete=models.SET_NULL, null=True, blank=True)
    singer = models.ForeignKey(Singer, on_delete=models.SET_NULL, null=True, blank=True)


class ShowOrderAcceptance(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    show = models.ForeignKey(ShowProfile, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateTimeField(null=True, blank=True)
