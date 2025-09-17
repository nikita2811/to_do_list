from django import forms

class TaskForm(forms.Form):
    task = forms.CharField(max_length=200, required=True)
    deadline = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    description = forms.CharField(widget=forms.Textarea, required=False)
    status = forms.ChoiceField(choices=[('To-Do', 'To-Do'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], required=True)