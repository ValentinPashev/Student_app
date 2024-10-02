from django.shortcuts import render

# Create your views here.

def add_event_page(request):
    return render(request, 'events/add_event_page.html')


def event_details_page(request, name_of_event:str):
    return render(request, 'events/event_details_page.html')


def edit_event_page(request,name_of_event:str):
    return render(request, 'events/edit_event_page.html')


def delete_event_page(request, name_of_event:str):
    return render(request, 'events/delete_event_page.html')