from  django.forms import ModelForm,Form
from  django import forms
from  django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User

from .models import Student,Subject,Grade

class AddFanlarForm(ModelForm):
    class Meta:
       model=Subject
       fields='__all__'


class AddOquvchiForm(ModelForm):
    class Meta:
        model=Student
        fields='__all__'


class AddbahoForm(ModelForm):
    class Meta:
        model=Grade
        fields='__all__'


class SignupFOrm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password1']




class UpdateGradeForm(ModelForm):
    class Meta:
        model=Grade
        fields=['grade']
        widgets={
            'grade':forms.NumberInput(attrs={'class':'form-control','min':2,'max':5})

        }







