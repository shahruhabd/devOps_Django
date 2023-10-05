from django import forms

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя', 'class': 'form-control'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя', 'class': 'form-control'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Введите адрес эл. почты', 'class': 'form-control'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль', 'class': 'form-control'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class RequestForm(forms.ModelForm):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Имя'})) 
    phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={
        'type': 'tel', 'class': 'form-control', 'placeholder': 'Номер телефона'}))
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Адрес эл. почты'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Описание проблемы'}))
    priority = forms.ChoiceField(
        label='Приоритет',
        choices=Request.PRIORITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Request
        fields = ['name', 'phone_number', 'email', 'description', 'priority']


class RequestUpdateForm(forms.ModelForm):
    resolve_action = forms.CharField(label='', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Решение проблемы'})) 
    status = forms.ChoiceField(
        label='Cтатус',
        choices=Request.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Request
        fields = ['resolve_action', 'status', 'assigned_user']

