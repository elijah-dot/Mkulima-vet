from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import  *
from django.forms import ModelForm

from datetime import datetime

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'email')

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields ='__all__'
        
class PetForm(forms.ModelForm):
  class Meta:
    model = Pet 
    fields = ('name','age','kind')
    # exclude=('user',)

class AppointmentForm(forms.ModelForm):

    years = range(datetime.now().year,datetime.now().year+1,1)
    


    date = forms.DateField(widget=forms.SelectDateWidget(years=years))
    
    class Meta:
        model = Appointment
        exclude = ['vet','pet_owner']

        labels = {
            'time_booked':'pick a time',
            'service': 'service',
            'pet':'pet',
        }
