from django.shortcuts import render
from .models import Task

import datetime
import time

# View for the home page where the table
# listing all created tasks are displayed.
def home(request):
    # checks if form was submitted
    if request.method == 'POST':
        # Retrieves user input on form to store
        # in the database.
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

        # Passes field values to instance
        # of Task modal.
        task = Task()
        task.title = title
        task.description = description
        task.created_on = created_on
        task.priority = priority
        task.started = started
        task.started_on = started_on
        task.completed = completed
        task.completed_on = completed_on
        
        # Inserts a new task record in the
        # tmsapp_task table in the
        # task_management_system database.
        task.save()

    # Retrieves all tasks and their corresponding
    # data from database to be displayed on the
    # home page table.
    all_tasks = Task.objects.all()
    context = { 'tasks' : all_tasks }
        
    return render(request, 'home.html', context)
