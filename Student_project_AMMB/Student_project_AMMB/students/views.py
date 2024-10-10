from django.shortcuts import render, redirect

from Student_project_AMMB.students.forms import RegistrationForm


# Create your views here.

def home(request):
    return render(request, 'students/home-page.html')

def index(request):
    return render(request, 'common/index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(index)

    else:
        form = RegistrationForm()

    context = {'form': form}

    return render(request, 'students/register-page.html', context)