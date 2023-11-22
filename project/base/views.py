from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib import messages

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Task

from .forms import UserCreationForm, CreateTask


@login_required(login_url="/login")
def main(request):
        if 's' in request.GET:
             s = request.GET['s']
             task = Task.objects.filter(user=request.user.id,title__contains=s)
             return render(request, 'main.html', {'task': task})
        else:
         tasklist = Task.objects.filter(user=request.user.id)
         return render(request, 'main.html', {'tasklist': tasklist})

@login_required(login_url="/login")
def edit(request,Task_id):
     task = Task.objects.get(pk=Task_id)
     form = CreateTask(request.POST or None,instance=task)
     if form.is_valid():
          form.save()
          return redirect('main')
     return render(request, 'edit.html' ,{'task':task,'form':form})

@login_required(login_url="/login")
def ShowTask(request,Task_id):
     task = Task.objects.get(pk=Task_id)
     return render(request, 'showtask.html' ,{'task':task})

@login_required(login_url="/login")
def DelTask(request,Task_id):
     taskdel = Task.objects.get(pk=Task_id)
     if request.method == 'POST':
        taskdel.delete()
        return redirect('main')
     
     return render(request,'deltask.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('main')
        else:
            messages.success(request, "Error!")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def RegisterPage(request):
    form = UserCreationForm

    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
                
    context = {'form' :form}
    return render(request, 'register.html', context)

@login_required(login_url="/login")
def Taskcreate(request):
    form = CreateTask

    if request.method == 'POST':
            form = CreateTask(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                return redirect('main')
                
    context = {'form' :form}
    return render(request, 'task_create.html', context)


     