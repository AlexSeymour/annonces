from django.forms import ModelForm
from django.contrib.auth.models import User
from user.models import Profile
from django import forms

class UserForm(ModelForm):
    password = forms.CharField(min_length=6, max_length=255, widget=forms.PasswordInput(attrs={'class':'form-control'}),
                               label="Nouveau mot de passe")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'})}


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'})}



class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'birth']
        widgets = {
            'birth': forms.SelectDateWidget(),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'phone':'Numéro de téléphone'
        }
