from django.urls import path

from Student_project_AMMB.accounts import views

urlpatterns = [

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

       ]
