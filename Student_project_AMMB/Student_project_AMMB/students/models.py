from django.db import models
from django.utils.text import slugify


# Create your models here.


class Student(models.Model):

    name = models.CharField(
        max_length=100
    )

    age = models.IntegerField(

    )

    faculty_number = models.IntegerField(

    )

    date_of_birth = models.DateField(

        blank=True,
        null=True
    )

    slug = models.SlugField(
        max_length=100,
        unique=True,
        null=True,
        blank=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.faculty_number}")

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name}-{self.faculty_number}"