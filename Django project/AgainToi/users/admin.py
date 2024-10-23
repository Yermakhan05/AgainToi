from django.contrib import admin

from users.models import UserProfile, UserOrder


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image', 'phone', 'address')
    search_fields = ('user',)


@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'status', 'total_price')
    search_fields = ('user',)
