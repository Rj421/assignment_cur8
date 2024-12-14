from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="Title"
    )
    
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control','id': 'id_content'}),
        label="Content"
    )