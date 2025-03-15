from django.db import models # type: ignore

# Create your models here.
class Task(models.Model):
    task =models.CharField(max_length=80)
    completed =models.BooleanField(default =False)
    create =models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.task
    

