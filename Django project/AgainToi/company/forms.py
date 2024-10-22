from django import forms
from .models import CompanyProfile

class VenueProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'location', 'capacity', 'venue_type']