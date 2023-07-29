from django import forms
from dashboard.models import BookDownloader

class Book_Download_Form(forms.ModelForm):
    class Meta:
        model = BookDownloader
        fields = ['user_name', 'phone_number', 'email']
        labels = {
            'user_name': 'Your Name',
            'phone_number': 'Phone Number',
            'email': 'Your Email',
        }