from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import User

class AddUserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username','email','password','cpass','address')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
            'password':forms.TextInput(attrs={'class':'form-control', 'type':'password','placeholder':'Enter your password'}),
            'cpass':forms.TextInput(attrs={'class':'form-control', 'type':'password','placeholder':'Renter your password'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your address'}),
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True ,'class':'form-control','placeholder':'Enter your name'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control','placeholder':'Enter your Password'})
    )