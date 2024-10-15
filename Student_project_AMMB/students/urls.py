from django.urls import path, include

from Student_project_AMMB.students import views

# urlpatterns = [
#     path('home/', views.home, name='home'),
#     path('index/', views.index, name='index'),
#     path('register/', views.register, name='register'),
#     path('<str:username>/<slug:slug>/', include([
#         path('',)
#     ]))
# ]

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('<str:name>/student/<slug:student_slug>/', include([
        path('', views.student_details_page, name='student-details'),
        path('edit/', views.student_edit_page, name='edit-student'),
        path('delete/', views.student_delete_page, name='delete-student'),
    ]))
]

#for accesing student details page the url link should look like this "students/Valentin%20Pashev/student/valentin-pashev-5/"
#                                                                                     ^^^^                         ^^^^
#                                                                                   name of the student   ||  slug of the student