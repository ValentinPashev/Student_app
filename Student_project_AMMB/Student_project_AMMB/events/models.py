from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    date = models.DateField(

    )

    location = models.CharField(
        max_length=200
    )

    organiser = models.CharField(
        max_length=200
    )
