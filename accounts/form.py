from django.contrib.auth.forms import UserCreationForm
from .models import UserInfoForm,books,bookissue
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model=UserInfoForm
        fields=['username','first_name','last_name','email','contact','age','gender','address','password1','password2']

class BooksForm(forms.ModelForm):
    
    class Meta: #provide the information
        model=books
        fields='__all__'
'''
class BooksIssueForm(forms.ModelForm):
    
    class Meta: #provide the information
        model=bookissue
        fields='__all__'
'''
class BooksIssueForm(forms.ModelForm):
    
    class Meta: #provide the information
        model=bookissue
        fields='__all__'