from django.db import models

# Create your models here.
class Tasks(models.Model):
    name = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name