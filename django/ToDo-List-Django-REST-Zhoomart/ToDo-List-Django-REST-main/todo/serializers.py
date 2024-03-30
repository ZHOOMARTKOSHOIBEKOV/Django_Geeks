from rest_framework import serializers
from todo.models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"
        read_only_fields = ["id", "created", "completed"]
