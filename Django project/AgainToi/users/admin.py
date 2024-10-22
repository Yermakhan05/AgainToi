from django.contrib import admin

from users.models import UserProfile


# Register your models here.

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'Bio', 'ProfilePicture')
    search_fields = ('Bio',)
