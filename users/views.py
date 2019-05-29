from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Person, Badge


# Create your views here.
def index(request):
    latest_person_list = Person.objects.order_by("-name")
    # template = loader.get_template('users/index.html')
    context = {"latest_person_list": latest_person_list}
    return render(request, "users/index.html", context)
    # return HttpResponse(template.render(context, request))


def detail(request, person_id):
    # try:
    # 	person = Person.objects.get(pk = person_id)
    # except Person.DoesNotExist:
    # 	raise Http404("Person is not in the system.")
    person = get_object_or_404(Person, pk=person_id)
    return render(request, "users/detail.html", {"person": person})


def badge(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, "users/badge.html", {"person": person})


def add_person(request):
    try:
        p_name = request.POST["name"]
    except (KeyError, Name.DoesNotExist):
        latest_person_list = Person.objects.order_by("-name")
        context = {
            "latest_person_list": latest_person_list,
            "error_message":      "Invalid Person Name",
        }
        return render(request, "users/index.html", context)
    else:
        latest_person_list = Person.objects.order_by("-name")
        for person in latest_person_list:
            person_name = person.name
            if p_name == person_name:
                context = {
                    "latest_person_list": latest_person_list,
                    "error_message":      "Person already exists",
                }
                return render(request, "users/index.html", context)
        p = Person(name=p_name)
        p.save()
        latest_person_list = Person.objects.order_by("-name")
        context = {"latest_person_list": latest_person_list}
        return render(request, "users/index.html", context)


def add_badge(request, person_id):
    error = ''
    person = get_object_or_404(Person, pk=person_id)
    # Tries and excepts must be changed so no blank badges can be entered
    try:
        b_name = request.POST["name"]
        b_presenter = request.POST["presenter"]
    except (KeyError, Name.DoesNotExist):
        return render(
            request,
            "users/badge.html",
            {"person": person, "error_message": "Invalid Badge Name."},
        )
    except (KeyError, Presenter.DoesNotExist):
        return render(
            request,
            "users/badge.html",
            {"person": person, "error_message": "Invalid Presenter Name."},
        )
    else:
        badge, created = Badge.objects.get_or_create(
            name=b_name,
            presenter=b_presenter
        )
        if badge.user_set.get(name=person.name):
            error = f'User has already obtained {badge}'
        else:
            badge.user_set.add(person)
            badge.save()

        return render(request, "users/detail.html",
                      {
                          "person": person,
                          "error_message":  error
                      },
                      )
