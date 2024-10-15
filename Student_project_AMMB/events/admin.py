from django.contrib import admin

from Student_project_AMMB.events.models import Event


# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'location', 'date', 'organiser']