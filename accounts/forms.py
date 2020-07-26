from django import forms 
from .models import Profile , City 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# profile form 
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']

#city form 

class CityForm(forms.ModelForm):
    
    class Meta:
        model = City
        fields = '__all__'
       
        

class SingupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['username','email','first_name','last_name',]
        
