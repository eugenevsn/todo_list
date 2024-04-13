from django import forms

from planner.models import Task, Tag


class TaskCreationForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.SelectDateWidget,
        required=False
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Task
        fields = "__all__"
