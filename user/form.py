from django import forms
from user.models import Customer
class CustomerForm(forms.ModelForm):
        class Meta:
               model=Customer
               fields="__all__"
               