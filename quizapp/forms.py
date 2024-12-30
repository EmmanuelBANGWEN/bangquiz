from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .models import CustomUser
from django.contrib.auth.models import User

from django_countries.fields import CountryField  # Importer CountryField


# class UserForm(UserCreationForm):
#     phone_number = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     #email = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

#     country = CountryField(blank_label='(Sélectionner un pays)').formfield(required=True, widget=forms.Select(attrs={'class': 'form-control'}))

#     class Meta:
#         model = CustomUser
#         fields = ['username', 'phone_number', 'country', 'password1', 'password2']
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
#         }


class RegistrationForms(forms.ModelForm):
    username = forms.CharField(label="Username", 
                               max_length=200, 
                               help_text='', 
                               required=True, 
                               widget=forms.TextInput(attrs={"type":"text", "id":"Username","class":"form-control",  "placeholder":"Username"}) )
    

    first_name = forms.CharField(label="First Name", 
                                 max_length=200, 
                                 help_text='', 
                                 required=True, 
                                 widget=forms.TextInput(attrs={"type":"text", "id":"FirstName","class":"form-control",  "placeholder":"First Name"}) )
    

    last_name = forms.CharField(label="Last Name", 
                                max_length=200, min_length=3,
                                help_text='', 
                                required=True, 
                                widget=forms.TextInput(attrs={"type":"text", "id":"LaststName", "class":"form-control",  "placeholder":"Last Name"}) )
    
    country = CountryField(blank_label='(Select your country)').formfield(
                                required=True, 
                                help_text='', 
                                widget=forms.Select(attrs={'class': 'form-control'}))


    email = forms.EmailField(label="Email", 
                             max_length=200, min_length=5,
                             help_text='', 
                             required=True, 
                            widget=forms.TextInput(attrs={"type":"text", "id":"emailAddress", "class":"form-control",  "placeholder":"Email Address"}) )
    

    password = forms.CharField(label="Password", 
                               max_length=200, min_length=8,
                               help_text='', 
                               required=True, 
                               widget=forms.TextInput(attrs={"type":"text", "id":"password", "class":"form-control",  "placeholder":"Password"}) )
    

    repeatpassword = forms.CharField(label="Repeat Password", 
                                     max_length=200, min_length=8,
                                     help_text='', 
                                     required=True, 
                                     widget=forms.TextInput(attrs={"type":"text", "id":"repeatpassword", "class":"form-control",  "placeholder":"Repeat Password"}) )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')













class AuthenticationForm(AuthenticationForm):
    class Meta:
        # model = CustomUser

        model = RegistrationForms
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
