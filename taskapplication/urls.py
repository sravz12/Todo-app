
"""taskapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from task.views import Indexview,Loginview,Registerview,AddTaskview, TaskDeleteView, TaskUpdateView,Tasklistview,TaskDEtailView, sign_out

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",Indexview.as_view()),
    path("",Loginview.as_view(),name="signin"),
    path("account/reg/",Registerview.as_view()),
    path("addtask/",AddTaskview.as_view(),name="todo-add"),
    path("task/all/",Tasklistview.as_view(),name="todo-list"),
    path("todo/<int:id>",TaskDEtailView.as_view(),name="todo-detail"),
    path("todo/<int:id>/delete",TaskDeleteView.as_view(),name="todo-delete"),
    path("account/logout/",sign_out,name="signout"),
    path("task/update/<int:id>",TaskUpdateView.as_view(),name="task-update")
]
