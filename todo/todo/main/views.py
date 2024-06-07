from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login
from . models import Task

# Create your views here.
def base(request):
    return render(request,'base.html')
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password')
        password2=request.POST.get('cpass')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                messages.info(request,'username already exists!!!')
                print("already have")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                return redirect(login)
        else:
            print("wrong password")        
    return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password1=request.POST.get('password')
        user=authenticate(request,username=username,password=password1)
        if user is not None:
            auth_login(request,user)
            return redirect(add)
        else:
            messages.info(request,'user not exists')
            print("user not exists")
            return redirect(login)    

    return render(request,'login.html')

def home(request):
    task=Task.objects.filter(is_completed=False)
    completed=Task.objects.filter(is_completed=True)
    context={
        'task':task,
        'complete':completed
    }
    return render(request,'add_task.html',context)

   
def add(request):

    if request.method=='POST':
        task=request.POST.get('task')
        Todo=Task.objects.create(task=task)
        Todo.save()
        return render(request,'home')
 