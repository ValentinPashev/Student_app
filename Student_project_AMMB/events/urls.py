from django.urls import path, include

from Student_project_AMMB.events import views

urlpatterns = [
    path('add/', views.add_event_page, name='events'),
    path('<str:name_of_event>/events/',
         include([

        path('', views.event_details_page, name='events'),

        path('edit/', views.edit_event_page, name='edit_event_page'),

        path('delete/', views.delete_event_page, name='delete_event_page'),

    ])),


    path('event_added/', views.event_created_page, name='event_created'),
]