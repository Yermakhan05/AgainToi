from django.db import models
from django.contrib.auth.models import User


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search_query = models.CharField(max_length=255)
    search_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} searched for '{self.search_query}' on {self.search_date}"


class EventType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.name