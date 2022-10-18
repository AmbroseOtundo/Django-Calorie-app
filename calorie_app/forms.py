from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Food, Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class SelectFoodForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('food_selected', 'quantity')

            # This function is a constructor for the SelectFoodForm class. 
            # It takes in a user object and then sets the queryset for the food_selected field to be all
            # the foods that belong to the user
            # user: the user who is logged in
            # One thing to watch is at the end __init__ is overridden. The reason is the queryset of the foods for selecting must be the foods that the user added. So we filtered Food objects by Food.objects.filter(person_of=user).
            # 
        def __init__(self, user, *args, **kwargs):
            user = kwargs.pop('user')
            super(SelectFoodForm, self).__init__(*args, **kwargs)
            self.fields['food_selected'].queryset = user

class AddFoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ('name','quantity','calorie')

   
class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('calorie_goal',)