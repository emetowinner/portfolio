from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    project = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name