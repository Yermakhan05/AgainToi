from django.contrib import admin
from company.models import CompanyProfile, CompanyOrderAcceptance, CompanyCalendar
from datetime import datetime


@admin.action(description='Accept selected orders')
def approve_orders(modeladmin, request, queryset):
    queryset.update(accepted=True, accepted_date=datetime.now())

@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company_name', 'address', 'capacity', 'venue_type')
    search_fields = ('user',)

@admin.register(CompanyCalendar)
class CompanyCalendarAdmin(admin.ModelAdmin):
    list_display = ('id', 'venue', 'event_name', 'event_date', 'description')
    search_fields = ('venue',)

@admin.register(CompanyOrderAcceptance)
class CompanyOrderAcceptanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'venue', 'accepted', 'accepted_date')
    search_fields = ('order',)
    actions = [approve_orders]  #
