from django.db import models


# Create your models here.

class Task(models.Model):
    id = models.IntegerField(primary_key=True, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    deadline = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False, blank=True, null=True)
    
    def __str__(self):
        return self.title


