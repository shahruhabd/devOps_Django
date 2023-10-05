from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.urls import reverse
from .forms import *
from django.http import HttpResponseRedirect
from .models import *
from django.contrib.auth.models import Group
from django.db.models import Count

def desk(request):
    resolved = 'RESOLVED'
    user = request.user
    is_tester = user.groups.filter(name='Tester').exists()

    if is_tester:
        requests = Request.objects.filter(status=resolved, assigned_user=user).order_by('created_at')
    else:
        requests = Request.objects.exclude(status=resolved).filter(assigned_user=user).order_by('created_at')
    return render(request, 'desk.html', {'requests': requests, 'user': user})

def create_request(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            reception_group = Group.objects.get(name='Editer')
            reception_users = reception_group.user_set.all()

            if reception_users.exists():
                assigned_user = min(reception_users, key=lambda user: user.assigned_requests.exclude(status='RESOLVED').count())
                request_new = form.save(commit=False)
                request_new.assigned_user = assigned_user
                request_new.save()
                messages.success(request, f'Зявка успешно создана! Ваш модератор {assigned_user.username}')
                return HttpResponseRedirect(reverse('desk'))
        else:
            messages.error(request, 'Ошибка при создании заявки. Пожалуйста, проверьте введенные данные.')
    else: 
        form = RequestForm()
    user = request.user
    return render(request, 'create_post.html', {'form':form,  'user': user})

def request_detail(request, pk): 
    request_detail = get_object_or_404(Request, pk=pk)
    form = RequestUpdateForm(request.POST or None, instance=request_detail)
    
    if form.is_valid():
        if request_detail.status == 'RESOLVED':
            reception_group = Group.objects.get(name='Tester')
            tester_users = reception_group.user_set.all()
            if tester_users.exists():
                tester_user = tester_users.first()
                request_detail.resolved_user = request_detail.assigned_user
                request_detail.assigned_user = tester_user
                form.save()
                messages.success(request, f'Заявка №{request_detail.id} решена и отправлена к Тестеру')
                return HttpResponseRedirect(reverse('desk'))

        else: 
            messages.success(request, f'Статус заявки №{request_detail.id} изменен на {request_detail.status}')
            form.save()
            
        return HttpResponseRedirect(reverse('desk'))
    user = request.user
    is_tester = user.groups.filter(name='Tester').exists()
    return render(request, 'request_detail.html', {'request_detail': request_detail, 'form': form, 'is_tester': is_tester})

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
    
