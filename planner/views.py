from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from planner.forms import TaskCreationForm
from planner.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")
    ordering = ["is_done", "-datetime"]


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("planner:index")
    form_class = TaskCreationForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("planner:index")
    form_class = TaskCreationForm


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("planner:index")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    success_url = reverse_lazy("planner:tag-list")
    fields = "__all__"


class TagUpdateView(generic.UpdateView):
    model = Tag
    success_url = reverse_lazy("planner:tag-list")
    fields = "__all__"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("planner:tag-list")


def toggle_task_complete(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return HttpResponseRedirect(reverse_lazy("planner:index"))
