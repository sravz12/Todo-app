from ast import Delete
from contextlib import redirect_stderr
import re
from django.shortcuts import render,redirect
from django.views.generic import View
from task.models import Tasks

# Create your views here.
class Indexview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class Loginview(View):
    def get(self,request,*args,**kwargas):
        return render(request,"login.html")
class Registerview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"register.html")
class AddTaskview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"task.html")
    def post(self,request,*args,**kwargs):
        # print(request.POST)
        name=request.POST.get("username")
        task=request.POST.get("task")
        Tasks.objects.create(user=name,task_name=task)
        return render(request,"task.html")
class Tasklistview(View):
    def get(self,request,*args,**kwargs):
        qs=Tasks.objects.all()
        return render(request,"takslist.html",{"todos":qs})

class TaskDEtailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        task=Tasks.objects.get(id=id) 
        return render(request,"task-details.html",{"todo":task})      

class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Tasks.objects.filter(id=id).delete()
        return redirect("todo-list")
        
