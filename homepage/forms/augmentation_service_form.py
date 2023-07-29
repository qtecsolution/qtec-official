from django import forms
from dashboard.models import AugmentationService


class AugmentationServiceForm(forms.ModelForm):
    class Meta:
        model = AugmentationService
        fields = ['name', 'company', 'phone', 'email', 'services', 'status', 'budget', 'description']

        widgets = {
            'description': forms.Textarea(attrs={'rows': 4})
        }