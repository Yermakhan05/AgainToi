from django.contrib import admin

from user.models import UserProfile, UserOrder, Address
from .models import User


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'user_type')
    search_fields = ('email',)


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'image', 'phone', 'address')
    search_fields = ('user',)


@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'status', 'total_price')
    search_fields = ('user',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'district_address', 'city')
    search_fields = ('city',)
