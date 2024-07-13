from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    number=models.CharField(max_length=150)
    alt=models.CharField(max_length=150)
    image=models.ImageField(upload_to='meadia')



























