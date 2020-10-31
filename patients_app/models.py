from django.db import models

# Create your models here.

class Patients(models.Model):
    name = models.CharField(max_length=50)
    docname = models.CharField(max_length=50)
    room = models.IntegerField()

    def __str__(self):
        self.name