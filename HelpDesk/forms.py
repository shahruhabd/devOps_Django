from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from HelpDesk.models import User

class UserLoginForm(AuthenticationForm):
    email = forms.TextInput(attrs={'placeholder': 'Введите почту'})
    password = forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(attrs={'placeholder': 'Вве'})
