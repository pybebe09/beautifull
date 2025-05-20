from profile import Profile

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Comment


class SignUpForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','password1','password2','email']

class ProfileForm(forms.Form):
    class Meta:
        model=Profile
        fields=['user.name','first_name','last_name','birth_date','bio','img']
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['text']