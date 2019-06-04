from django.shortcuts import render, get_object_or_404, redirect
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
    # Construct context
    page_context = {
        'latest_person_list': Person.objects.order_by('-name'),
        'error_message': None
    }

    person_name = request.POST.get('name', '')

    if not person_name:
        page_context['error_message'] = 'Username field must not be left blank'
        # TODO: create a user_add page not tied into the index
        return render(request, 'users/index.html', page_context)
    else:
        new_person = Person(name=person_name)
        new_person.save()

    return redirect('users:index')


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
        badge, _ = Badge.objects.get_or_create(
            name=b_name,
            presenter=b_presenter
        )
        if badge.user_set.filter(name=person.name):
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
