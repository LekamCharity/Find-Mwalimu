from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    tutors = Tutor.display_tutor()
    return render(request, "index.html", {"tutors":tutors}) 


def tutor(request,tutor_id):
    try:
        tutor = Tutor.objects.filter(id = tutor_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"mwalimu.html", {"tutor":tutor})


def location(request):
    if 'tutor' in request.GET and request.GET["tutor"]:
        search_term = request.GET.get("tutor")
        searched_tutors = Tutor.find_tutor_location(search_term)
        message = f"{search_term}"
        return render(request, 'location.html',{"message":message,"tutors": searched_tutors})
    else:
        message = "Project does not exist"
        return render(request, 'location.html',{"message":message})
    return render(request, "location.html")


def name(request):
    if 'tutor' in request.GET and request.GET["tutor"]:
        search_term = request.GET.get("tutor")
        searched_tutors = Tutor.find_tutor_name(search_term)
        message = f"{search_term}"
        return render(request, 'mwalimus_name.html',{"message":message,"tutors": searched_tutors})
    else:
        message = "Project does not exist"
        return render(request, 'mwalimus_name.html',{"message":message})
    return render(request, "mwalimus_name.html")

def experience(request):
    if 'tutor' in request.GET and request.GET["tutor"]:
        search_term = request.GET.get("tutor")
        searched_tutors = Tutor.find_programming_experience(search_term)
        message = f"{search_term}"
        return render(request, 'mwalimus_experience.html',{"message":message,"tutors": searched_tutors})
    else:
        message = "Project does not exist"
        return render(request, 'mwalimus_experience.html',{"message":message})
    return render(request, "mwalimus_experience.html")