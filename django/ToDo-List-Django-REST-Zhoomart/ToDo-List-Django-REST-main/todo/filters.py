from todo.models import TodoList
from django_filters import rest_framework as dj_filters


class TodoListFilterSet(dj_filters.FilterSet):
    tasks = dj_filters.CharFilter(field_name="tasks", lookup_expr="icontains")
    status = dj_filters.CharFilter(field_name="status", lookup_expr="exact")

    order_by_field = "ordering"

    class Meta:
        model = TodoList
        fields = [
            "tasks",
            "status",
        ]
