from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return f"{self.content}. is done: {self.is_done}."


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
