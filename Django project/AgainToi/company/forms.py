from django import forms

from user.models import Address
from .models import CompanyProfile


class VenueProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ['company_name', 'address', 'capacity', 'venue_type']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['region', 'city']
