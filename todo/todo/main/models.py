from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=255,default='default task')
    is_completed=models.BooleanField(default=False)
    created_date=models.DateField(auto_now_add=True)
    updated_now=models.DateField(auto_now=True)