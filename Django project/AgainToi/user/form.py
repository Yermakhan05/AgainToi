from django import forms
from .models import Address, Region, City


class AddressForm(forms.ModelForm):
    # region = forms.ModelChoiceField(queryset=Region.objects.all(), required=True, label="Region")
    # city = forms.ModelChoiceField(queryset=City.objects.none(), required=True, label="City")

    class Meta:
        model = Address
        fields = ['region', 'city']
