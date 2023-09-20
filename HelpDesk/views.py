from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import *
from django.http import HttpResponseRedirect
from .models import *

def desk(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            request_new = form.save(commit=False)
            request_new.save()
            messages.success(request, 'Зявка успешно создана!')
            return HttpResponseRedirect(reverse('desk'))
    else: 
        form = RequestForm()
    requests = Request.objects.order_by('created_at')
    return render(request, 'desk.html', {'form':form, 'requests': requests})

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегистрированы!')
            return HttpResponseRedirect(reverse('login'))
    else: 
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'registration.html', context)

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            messages.success(request, 'Успешный вход в аккаунт!')
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('desk'))
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('login')
    
