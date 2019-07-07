from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if email and User.objects.filter(email=email).count() > 0:
    #         raise forms.ValidationError(f"The Email you provided is already taken by another user.Please provide another email.")
    #     return email

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(f'A user with the email "{email}" already exists.')
        return email


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(label='')

    class Meta:
        model = Profile
        fields = ['image']
