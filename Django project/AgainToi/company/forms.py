from django import forms
from .models import CompanyProfile


class VenueProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'address', 'capacity', 'venue_type']
