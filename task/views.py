
from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DetailView,UpdateView

from task.models import Tasks
from task.forms import LoginForm,RegistrationForm,TaskUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Create your views here.
def signin_reqired(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
class Indexview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class Loginview(View):
    def get(self,request,*args,**kwargas):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("todo-list")
            else:
                messages.error(request,"invalid credentials")
                return render(request,"login.html",{"form":form})



class Registerview(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"registration has completed")
            return redirect("signin")
        else:
            messages.error(request,"ragistration failed")
            return redirect(request,"register.html",{"form":form})


@method_decorator(signin_reqired,name="dispatch")
class AddTaskview(View):
    def get(self,request,*args,**kwargs):
        return render(request,"task.html")
    def post(self,request,*args,**kwargs):
        # print(request.POST)
        user=request.user
        task=request.POST.get("task")
        Tasks.objects.create(user=user,task_name=task)
        messages.success(request,"task has been created")
        return redirect("todo-list")
@method_decorator(signin_reqired,name="dispatch")
class Tasklistview(ListView):
    model=Tasks
    template_name="tasklist.html"
    context_object_name="todos"
    def get_queryset(self):
        return Tasks.objects.filter(user=self.request.user)
    # def get(self,request,*args,**kwargs):
    #     if request.user.is_authenticated:
    #         qs=Tasks.objects.filter(user=request.user)
    #         return render(request,"takslist.html",{"todos":qs})
    #     else:
    #         return redirect("signin")

class TaskDEtailView(DetailView):
    model=Tasks
    template_name="task-details.html"
    context_object_name="todo"
    pk_url_kwarg="id"

    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     task=Tasks.objects.get(id=id) 
    #     return render(request,"task-details.html",{"todo":task})      

class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Tasks.objects.filter(id=id).delete()
        messages.success(request,"task deleted")
        return redirect("todo-list")
@signin_reqired
def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

class TaskUpdateView(UpdateView):
    model=Tasks
    form_class=TaskUpdateForm
    template_name="task-update.html"  
    pk_url_kwarg="id" 
    success_url=reverse_lazy("todo-list")  

    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     qs=Tasks.objects.get(id=id)


