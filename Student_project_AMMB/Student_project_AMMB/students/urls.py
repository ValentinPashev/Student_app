from django.urls import path

from Student_project_AMMB.students import views

urlpatterns = [
    path('home/', views.home, name='home'),
]