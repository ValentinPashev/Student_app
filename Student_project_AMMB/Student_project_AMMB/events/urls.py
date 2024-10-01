from django.urls import path

from Student_project_AMMB.events import views

urlpatterns = [
    path('event/', views.events, name='events'),
]