from django.shortcuts import render
from .forms import TaskForm
from .models import Task
from django.http import HttpResponse

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    if tasks:
        return render(request, 'index.html', {'tasks': tasks})
    else:
       return render(request, 'index.html', {})
    

def create(request):
   if request.method == 'POST':
       form = TaskForm(request.POST)
       if form.is_valid():
           task = form.cleaned_data['task']
           deadline = form.cleaned_data['deadline'] # Corrected field name
           description = form.cleaned_data['description']       
           status = form.cleaned_data['status']

           task_instance = Task(task=task, deadline=deadline, description=description, status=status)
           task_instance.save()
           tasks = Task.objects.all()
           if tasks:
            return render(request, 'index.html', {tasks: tasks})
           else :
            return render(request, 'index.html', {})
           
   else:
       form = TaskForm()    
       return render(request, 'index.html', {'form': form})
   
   
   
def task_detail(request,task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'taskDetails.html', {'task': task})


def delete_task(request,task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    tasks = Task.objects.all()
    if tasks:
     return render(request, 'index.html', {tasks: tasks})
    else :
       return render(request, 'index.html', {})

def edit_task(request,task_id):
   task = Task.objects.get(id=task_id)
   return render(request, 'updateTask.html', {'task': task})  

def update_task(request,task_id):
    tasks = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task = request.POST.get('task')
        deadline = request.POST.get('deadline') # Corrected field name
        description = request.POST.get('description')      
        status = request.POST.get('status')
        # Update the task fields if data is provided
        if tasks:
            tasks.task = request.POST.get('task')
        if description is not None:
            tasks.description = description
        if status:
            tasks.status = status
        if deadline:
            tasks.deadline = deadline

        tasks.save()  # Save changes to the database
        tasks = Task.objects.all()
        if tasks:
            return render(request, 'index.html', {tasks: tasks})
        else :
            return render(request, 'index.html', {})
   


