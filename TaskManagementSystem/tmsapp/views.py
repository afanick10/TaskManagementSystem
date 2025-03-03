from django.shortcuts import redirect, render
from .models import Task

import datetime
import time

# Create your views here.
def home(request):
    if request.method == 'POST':
        post_request = request.POST
        title = post_request.get('task_title')
        description = post_request.get('task_description')
        priority = post_request.get('priority_select')
        started = post_request.get('started_checkbox') != None
        
        time_stamp = time.time()
        created_on = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
        
        started_on = created_on if started else 'Not started'
        completed = False
        completed_on = 'Not completed'

        task = Task()
        task.title = title
        task.description = description
        task.created_on = created_on
        task.priority = priority
        task.started = started
        task.started_on = started_on
        task.completed = completed
        task.completed_on = completed_on
        
        task.save()

    all_tasks = Task.objects.all()
    context = { 'tasks' : all_tasks }
        
    return render(request, 'home.html', context)
