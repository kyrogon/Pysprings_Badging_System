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


def person_detail(request, person_id):
    # try:
    # 	person = Person.objects.get(pk = person_id)
    # except Person.DoesNotExist:
    # 	raise Http404("Person is not in the system.")
    person = get_object_or_404(Person, pk=person_id)
    return render(request, "users/user_detail.html", {"person": person})


def badge_detail(request, badge_id):
    badge = get_object_or_404(Badge, pk=badge_id)
    return render(request, "users/badge_detail.html", {"badge": badge})


def add_person(request):
    latest_person_list = Person.objects.order_by("-name")
    p_name = request.POST.get('name', '')
    if not p_name:
        return render(
            request,
            'users/index.html',
            {
                'error_message': "name field must not be left blank",
                'latest_person': latest_person_list,
            },
        )
    else:
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


def add_badge(request):
    error = ''

    if request.method == 'POST':
        # Get field values or empty string
        b_name = request.POST.get('name', '')
        b_presenter = request.POST.get('presenter', '')

        # return a warning if any fields were left blank
        if '' in (b_name, b_presenter):
            return render(
                request,
                'users/add_badge.html',
                {
                    'error_message':
                        'Neither badge name or presenter may be left blank'
                },
            )
        else:
            badge, _ = Badge.objects.get_or_create(
                name=b_name,
                presenter=b_presenter
            )
            # if badge.user_set.filter(name=person.name):
            #     error = f'User has already obtained {badge}'
            # else:
            #     badge.user_set.add(person)
            badge.save()

    return render(
        request,
        "users/add_badge.html",
        {
            "error_message": error
        },
    )
