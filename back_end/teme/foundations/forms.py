from typing import Any
from django.forms import ModelForm

from foundations import models
from nonprofits.models import Nonprofit

class FoundationForm(ModelForm):
    class Meta:
        model = models.Foundation
        fields = ['name', 'email']

    def clean(self):
        email = self.cleaned_data.get('email')
        if not email:
            self.add_error('email', 'Email is required')

        if models.Foundation.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already in use')

        if Nonprofit.objects.filter(email=email).exists():
            self.add_error('email', 'This email is already in use by a Nonprofit')

        return super().clean()
    
