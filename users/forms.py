from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  

# Create forms here
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'prompt srch_explore'}), max_length=50, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class': 'prompt srch_explore'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'prompt srch_explore'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']



class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField (required=True)
    job_title = forms.CharField (required=True, 
                             widget=forms.TextInput(attrs={'class':'input',
                                                          'placeholder':'Job Title'})
                            )

    class Meta:
        model = Profile
        fields = ['image', 'full_name', 'phone_number']