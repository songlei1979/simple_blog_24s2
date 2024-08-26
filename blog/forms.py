from django import forms
from blog.models import Post


class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'author')

        widgets = {
            'title': forms.TextInput(attrs={'id':'title','class': 'form-control', 'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control', 'id': 'author'}),
        }
