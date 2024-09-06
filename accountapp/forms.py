from django.forms import *
from .models import *

class CustomerForm(ModelForm):
    class Meta:
        model=CustomerModel
        fields='__all__'
        widgets={
            'gender':RadioSelect(choices=[("Male","Male"),("Female","Female")]),
            'birthdate':DateInput(attrs={'type':'date'}),
            'address':Textarea(attrs={'rows':3})
        }

class CustomerLoginForm(ModelForm):
    class Meta:
        model=CustomerLoginModel
        fields=['email','password']
        widgets={
            'password':PasswordInput()
        }

class NewAccountForm(ModelForm):
    class Meta:
        model=AccountModel
        fields=['account_type','account_owner']
        widgets={
            'account_type':Select(choices=[('Current Account','Current Account'),
                                           ('Saving Account','Saving Account'),
                                           ('PPF Account','PPF Account'),
                                           ('Salary Account','Salary Account'),]),
            'account_owner':RadioSelect(choices=[("Single Owner","Single Owner"),("Joined Owner","Joined Owner")])
        }