from django import forms
from .models import Fish


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Fish
        fields = '__all__'
        exclude = ['fish_id','timestamp']