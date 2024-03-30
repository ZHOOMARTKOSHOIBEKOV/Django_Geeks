from django.contrib import admin
from todo.models import TodoList

admin.site.site_url = "http://127.0.0.1:8000/"


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "tasks",
        "created",
        "deadline",
        "completed",
        "status",
    ]
    list_filter = ["status"]
    readonly_fields = ["created", "completed"]
    search_fields = ("id", "tasks")
    ordering = ["deadline"]
