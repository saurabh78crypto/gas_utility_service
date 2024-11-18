from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'description', 'attachment']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'request_type': forms.Select(attrs={'class': 'form-control'}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
