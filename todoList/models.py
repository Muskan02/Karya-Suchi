from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
    	return self.title + ' | ' + str(self.completed)

class theme(models.Model):
	light = models.BooleanField(default=True)
