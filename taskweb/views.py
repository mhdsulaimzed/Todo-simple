from django.shortcuts import render,redirect
from django.views.generic import View
from taskweb.forms import Userform,Loginform,Taskform,TaskEditForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from api.models import Task
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.

def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            return redirect('signin')
        else:
            return fn(request,*args,**kw)
    return wrapper

class SingupView(View):
    def get(self,request,*args,**kw):
        forms=Userform()
        
        return render(request,"register.html",{"forms":forms})
    def post(self,request,*args,**kw):
        form=Userform(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request,"register.html",{"form":form})
class LoginView(View):
    def get(self,request,*args,**kw):
        form=Loginform()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kw):
        form=Loginform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})


@method_decorator(signin_required,name="dispatch")           
class IndexView(View):
    def get(self,request,*args,**kw):
        
        return render(request,"index.html")


@method_decorator(signin_required,name="dispatch")
class TaskCreateView(View):
    def get(self,request,*args,**kw):
        form=Taskform()
        return render(request,"task-add.html",{"form":form})
    def post(self,request,*args,**kw):
        form=Taskform(request.POST)
        if form.is_valid():
          
            form.instance.user=request.user
            form.save()
            print("saved")
            messages.success(request,"Task added")
            return redirect("task-list")
        else:
            return render(request,"task-add.html",{"form":form})


@method_decorator(signin_required,name="dispatch")
class TaskListView(View):
    def get(self,request,*args,**kw):
        qs=Task.objects.filter(user=request.user)
        return render(request,"task-list.html",{"tasks":qs})


@method_decorator(signin_required,name="dispatch")
class TaskDetailView(View):

    def get(self,request,*args,**kw):
        id=kw.get("id")
        qs=Task.objects.get(id=id)
        return render (request,"task-detail.html",{"tasks":qs})


@method_decorator(signin_required,name="dispatch")
class TaskDeleteView(View):
    def get(self,request,*args,**kw):
        id=kw.get("id")
        Task.objects.filter(id=id).delete()
        messages.success(request,"Task Deleted")
        return redirect("task-list")


@method_decorator(signin_required,name="dispatch")
class TaskEditView(View):
    def get(self,request,*args,**kw):
        id=kw.get("id")
        obj=Task.objects.get(id=id)
        form=TaskEditForm(instance=obj)
        return render(request,"task-edit.html",{"form":form})

    def post(self,request,*args,**kw):
        id=kw.get("id")
        obj=Task.objects.get(id=id)
        
        form=TaskEditForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request,"Task Updated")
            return redirect("task-list")
        else:
            return render(request,"task-edit.html",{"form":form})



@method_decorator(signin_required,name="dispatch")
class LogoutView(View):
    def get(self,request,*args,**kw):
        logout(request)
        return redirect("signin")

             




