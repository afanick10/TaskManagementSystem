from django.db import models

import datetime
import time

# Model that contains all the properties for a task.
class Task:
    def __init__(self,
                 title,
                 description,
                 created_by,
                 created_on,
                 priority,
                 started,
                 started_on,
                 completed,
                 completed_on):
        self.title = title
        self.description = description
        self.created_by = created_by
        self.created_on = created_on
        self.priority = priority
        self.started = started
        self.started_on = started_on
        self.completed = completed
        self.completed_on = completed_on
    
    def click_started(self):
        self.started = True
        time_stamp = time.time()
        self.started_on = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')
    
    def click_completed(self):
        self.completed = True
        time_stamp = time.time()
        self.completed_on = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M:%S')

