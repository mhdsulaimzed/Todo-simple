from django.db import models
from django.contrib.auth.models import User 

class Task(models.Model):
    task_name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    status=models.BooleanField(default=False)

    def __str__(self) :
        return self.task_name

