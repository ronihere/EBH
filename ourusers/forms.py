from django import forms
# from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from .models import UserProfile

class userregistrationform(UserCreationForm):
    email=forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
# class UserProfileForm(ModelForm):
#     class Meta:
#         model=UserProfile
#         fields=['fname','lname','img','address']