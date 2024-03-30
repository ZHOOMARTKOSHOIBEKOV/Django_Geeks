from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)

from rest_framework import viewsets, mixins
from rest_framework.schemas.openapi import AutoSchema

from todo.filters import TodoListFilterSet
from todo.models import TodoList
from todo.serializers import TodoListSerializer


def start(request):
    return render(request, "start.html")


class TodoListView(ListView):
    context_object_name = "todolist_"
    model = TodoList
    template_name = "todolist_list.html"


class TodoListViewActive(ListView):
    context_object_name = "todolist_"
    queryset = TodoList.objects.filter(status=False)
    template_name = "todolist_list_not_active.html"


class TodoDetailView(DetailView):
    context_object_name = "todolist"
    model = TodoList
    template_name = "todolist_detail.html"


class TodoCreateView(CreateView):
    model = TodoList
    fields = ["tasks", "status", "deadline"]
    template_name = "todolist_create.html"
    success_url = "/todolist/"


class TodoUpdateView(UpdateView):
    model = TodoList
    fields = ["tasks", "status", "deadline"]
    template_name = "todolist_update.html"
    success_url = "/todolist/"


class TodoDeleteView(DeleteView):
    model = TodoList
    template_name = "todolist_delete.html"
    success_url = "/todolist/"


# DRF


class TodoViewSet(
    mixins.ListModelMixin,  # GET /todolist
    mixins.CreateModelMixin,  # POST /todolist
    mixins.RetrieveModelMixin,  # GET /todolist/1
    mixins.DestroyModelMixin,  # DELETE /todolist/1
    mixins.UpdateModelMixin,  # PUT /todolist/1
    viewsets.GenericViewSet,
):
    queryset = TodoList.objects.all().order_by("id")
    serializer_class = TodoListSerializer
    filterset_class = TodoListFilterSet

    schema = AutoSchema(
        tags=["TodoList"],
        component_name="TodoList",
        operation_id_base="TodoList",
    )
