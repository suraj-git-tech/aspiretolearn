# In your forms.py file
from django import forms
from .models import Post

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','cols':"30" ,'rows':"5"}))

class LogInForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']
