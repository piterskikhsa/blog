from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "simple_input", "placeholder": "Введите название статьи"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "post-content"}))
