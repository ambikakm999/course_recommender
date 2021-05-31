from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','topics_of_interest']


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class RateForm(ModelForm):
    #RATE_CHOICES = [('like', 'Like'),
                   # ('dislike', 'Dislike'),]
    #rating = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.RadioSelect())
    class Meta:

        model=Rating
        #rating = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.RadioSelect())
        fields=['rating']
        widgets = {
            'rating': forms.RadioSelect()
        }
        #favorite_fruit = forms.CharField(label='What is your favorite fruit?',
                                        # widget=forms.RadioSelect(choices=FRUIT_CHOICES))

