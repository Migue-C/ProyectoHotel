from django import forms

from .models import Hotel

class PostForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('title', 'text', 'author', 'published_date')