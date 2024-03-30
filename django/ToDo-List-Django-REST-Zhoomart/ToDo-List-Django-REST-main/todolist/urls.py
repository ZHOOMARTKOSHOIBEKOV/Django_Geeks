"""todolist URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

from todo import views
from todo.views import (
    TodoListView,
    TodoListViewActive,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.start),
    path("api/", include("todo.urls")),
    path("todolist/", TodoListView.as_view(), name="index"),
    path("todolist/not-active/", TodoListViewActive.as_view()),
    path("todolist/<int:pk>", TodoDetailView.as_view(), name="detail"),
    path("todolist/create/", TodoCreateView.as_view(), name="create"),
    path("todolist/update/<int:pk>", TodoUpdateView.as_view(), name="update"),
    path("todolist/delete/<int:pk>", TodoDeleteView.as_view(), name="delete"),
    path(
        "openapi/",
        get_schema_view(
            title="ToDo List",
            description="API for all things …",
            version="1.0.0",
        ),
        name="openapi-schema",
    ),
]
