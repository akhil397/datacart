from django import forms
from .models import CodeModels

class CodeForm(forms.ModelForm):
    class Meta:
        model = CodeModels
        fields = ['title', 'language', 'codes', 'description', 'types', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'language': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter programming language'}),
            'codes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter code'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'types': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter type'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
class SearchForm(forms.Form):
    query = forms.CharField(label='Search',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Search by title, language, or type...'}),
    required=False
    )
    language = forms.CharField(label='Filter by Language',widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Filter by language...'}),
    required=False
    )