from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    print("METHOD:", request.method)
    print("POST:", request.POST)
    tasks=Task.objects.all()
    search_query=request.POST.get('search')
    print(search_query)
    if search_query:
        tasks=Task.objects.filter(title__icontains=search_query)
    context={'tasks':tasks}
    return render(request,'todos/tasks.html',context)

@login_required(login_url='')
def create_task(request):
    if request.method=='POST':
        title=request.POST.get('title')
        Task.objects.create(title=title)
    return redirect('list-tasks')

@login_required(login_url='')
def delete_task(request,id):
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('list-tasks')

@login_required(login_url='')
def update_task(request,id):
    task=Task.objects.get(id=id)
    context={'task':task}
    if request.method=='POST':
        newTitle=request.POST.get('title')
        task.title=newTitle
        task.save()
        return redirect('list-tasks')
    return render(request,'todos/edit-task.html',context)

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            User.objects.create_user(username=username,email=email,password=password1)
            messages.success(request,'account created successfully')
            return redirect('login')
        else:
            messages.error(request,'passwords do not match')
    return render(request,'todos/register.html')