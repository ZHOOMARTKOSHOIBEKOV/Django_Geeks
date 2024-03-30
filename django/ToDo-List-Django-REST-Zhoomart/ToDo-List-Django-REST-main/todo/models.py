from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils import timezone


class TodoList(models.Model):
    tasks = models.CharField(max_length=250, help_text="Задание:")
    status = models.BooleanField(default=False, help_text="Статус выполнения:")
    created = models.DateTimeField(default=timezone.now(), help_text="Задание создано:")
    deadline = models.DateTimeField(
        default=timezone.now() + timedelta(days=7),
        help_text="Выполнить до (по умолчанию 7 дней):",
    )
    completed = models.DateTimeField(
        default=None,
        null=True,
        blank=True,
        help_text="Задание переведено в статус 'Выполнено':",
    )

    def get_absolute_url(self):
        return reverse("todolist", args=[self.id])

    def save(self, *args, **kwargs) -> None:
        if self.status is False:
            self.completed = None
        else:
            if self.completed is None:
                self.completed = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"TodoList {self.id}|{self.tasks}|{self.status}|{self.created}|{self.completed}"
