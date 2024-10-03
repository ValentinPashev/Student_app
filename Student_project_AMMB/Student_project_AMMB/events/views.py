from django.shortcuts import render, redirect

from Student_project_AMMB.events.forms import EventBaseForm


# Create your views here.

def add_event_page(request):

    form = EventBaseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('event_created')

    context = {'form': form}

    return render(request, 'events/add_event_page.html', context)

def event_details_page(request, name_of_event:str):
    return render(request, 'events/event_details_page.html')


def edit_event_page(request,name_of_event:str):
    return render(request, 'events/edit_event_page.html')


def delete_event_page(request, name_of_event:str):
    return render(request, 'events/delete_event_page.html')

def event_created_page(request):
    return render(request, 'events/page_added.html')