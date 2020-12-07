from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    tutors = Tutor.display_tutor()
    return render(request, "template", {"tutors":tutors}) 


def tutor(request,tutor_id):
    try:
        tutor = Tutor.objects.filter(id = tutor_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"template", {"tutor":tutor})


def location(request):
    if 'tutor' in request.GET and request.GET["tutor"]:
        search_term = request.GET.get("tutor")
        searched_tutors = Tutor.find_tutor_location(search_term)
        message = f"{search_term}"
        return render(request, 'template',{"message":message,"tutors": searched_tutors})
    else:
        message = "Project does not exist"
        return render(request, 'template',{"message":message})
    return render(request, "template")


def name(request):
    if 'tutor' in request.GET and request.GET["tutor"]:
        search_term = request.GET.get("tutor")
        searched_tutors = Tutor.find_tutor_name(search_term)
        message = f"{search_term}"
        return render(request, 'template',{"message":message,"tutors": searched_tutors})
    else:
        message = "Project does not exist"
        return render(request, 'template',{"message":message})
    return render(request, "template")

def experience(request):
    if 'tutor' in request.GET and request.GET["tutor"]:
        search_term = request.GET.get("tutor")
        searched_tutors = Tutor.find_programming_experience(search_term)
        message = f"{search_term}"
        return render(request, 'template',{"message":message,"tutors": searched_tutors})
    else:
        message = "Project does not exist"
        return render(request, 'template',{"message":message})
    return render(request, "template")