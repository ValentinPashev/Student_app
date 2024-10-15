from django.contrib import admin

from Student_project_AMMB.students.models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'faculty_number', 'date_of_birth']