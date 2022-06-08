from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta: 
        model = Blog
        fields = ['title', 'subtitle', 'body','header_image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'subtitle': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'header_image': forms.FileInput(attrs={'class':'form-control'})
        }