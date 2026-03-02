from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=60)
    password = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name
    