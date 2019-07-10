from django import forms
from .models import Address


class AddressesForm(forms.ModelForm):
    class Meta:

        model = Address
        fields = ['address_1', 'address_2', 'city',
                  'state', 'country', 'post_code']

        widgets = {
            'address_1': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
        widgets = {
            'address_2': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
        widgets = {
            'city': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
        widgets = {
            'state': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
        widgets = {
            'country': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
        widgets = {
            'post_code': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }
        widgets = {
            'phone': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }