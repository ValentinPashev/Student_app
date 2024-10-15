from django.db import models
from django.utils.text import slugify


# Create your models here.


class Student(models.Model):

    name = models.CharField(
        max_length=100
    )

    age = models.IntegerField(

    )

    faculty_number = models.CharField(

    )

    date_of_birth = models.DateField(

        blank=True,
        null=True
    )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False,
    )

    email = models.EmailField(
        "email address",
        blank=True)

    password = models.CharField(
        max_length=100,
    )

    profile_picture = models.URLField(
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name}-{self.id}"