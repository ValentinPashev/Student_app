from django.http import HttpResponse
from django.shortcuts import render, redirect

from Student_project_AMMB.students.forms import StudentAddForm
from Student_project_AMMB.students.models import Student


# Create your views here.

def home(request):
    return render(request, 'students/home-page.html')

def index(request):
    return render(request, 'common/index.html')

def add_student(request):
    form = StudentAddForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form
    }

    return render(request, 'students/register-page.html', context)


    # if request.method == 'POST':
    #     if form.is_valid():
    #         user = form.save()
    #         return redirect(index)
    #
    # context = {'form': form}
    #
    # return render(request, 'students/register-page.html', context)


def student_details_page(request, name, student_slug):
    student = Student.objects.get(slug=student_slug)

    if student:
        return HttpResponse('The student was found')

    else:
        return HttpResponse('The student was not found')




def student_edit_page(request):
    return None


def student_delete_page(request, username, slug):
    student = Student.objects.get(name=username, slug=slug)