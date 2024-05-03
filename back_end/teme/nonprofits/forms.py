from typing import Any
from django.forms import ModelForm

from foundations.models import Foundation
from nonprofits.models import Nonprofit

class NonProfitForm(ModelForm):
    class Meta:
        model = Nonprofit
        fields = ['name', 'address', 'email']

    def clean(self):
        email = self.cleaned_data.get('email')
        address = self.cleaned_data.get('address')
        if not email:
            self.add_error('email', 'Email is required')

        if len(address) > 100:
            self.add_error('address', 'Address is too long')

        if Nonprofit.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already in use')

        if Foundation.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already in use by a Foundation')

        return super().clean()
    
