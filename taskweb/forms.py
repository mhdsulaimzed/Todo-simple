from django import forms
from django.contrib.auth.models import User
from api.models import Task

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","email"]
class Loginform(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
class Taskform(forms.ModelForm):

    class Meta:
        model=Task
        fields=["task_name"]
        widgets={"task_name":forms.TextInput(attrs={"class":"form-control"})}

class TaskEditForm(forms.ModelForm):

    class Meta:
        model=Task
        fields=["task_name","status"]
        