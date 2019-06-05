from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Person, Badge
from .forms import BadgeForm


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
        'error_message':      None,
    }

    person_name = request.POST.get('name', '')

    if not person_name:
        page_context['error_message'] = 'Username field must not be left blank'
        return render(request, 'users/index.html', page_context)

    new_person = Person(name=person_name)
    new_person.save()

    return redirect('users:index')


# def add_badge(request, person_id):
#     # construct context
#     person = get_object_or_404(Person, pk=person_id)
#     page_context = {
#         'person': person,
#         'error_message': None,
#     }
#
#     # get values from the page form
#     badge_name = request.POST.get('name', '')
#     badge_presenter = request.POST.get('presenter', '')
#
#     # verify that form fields have be filled
#     if not (badge_name or badge_presenter):
#         page_context['error_message'] = 'Neither form field may be left blank'
#     else:
#         new_badge, _ = Badge.objects.get_or_create(
#             name=badge_name,
#             presenter=badge_presenter,
#         )
#         new_badge.user_set.add(person)
#         new_badge.save()
#
#     return render(request, 'users/badge.html', page_context)


def badge_list(request):
    badges = Badge.objects.all()
    context = {
        'badge_list': badges
    }

    return render(request, 'users/badge_list.html', context)


def badge_form(request, badge_id=None):
    if badge_id:
        badge_instance = Badge.objects.get(pk=badge_id)
    else:
        badge_instance = None

    if request.method == 'POST':
        form = BadgeForm(request.POST, instance=badge_instance)
        if form.is_valid():
            new_badge = form.save()
            return redirect('users:badge_detail', new_badge.id)
    elif badge_id:
        form = BadgeForm(instance=badge_instance)
    else:
        form = BadgeForm()

    return render(request, 'users/add_badge.html', {'form': form})


def badge_detail(request, badge_id):
    badge = Badge.objects.get(pk=badge_id)
    if request.GET.get('edit', False):
        return redirect('users:edit_badge', badge_id=badge.id)
    return render(request, 'users/badge_detail.html', {'badge': badge})
