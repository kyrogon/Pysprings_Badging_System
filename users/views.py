from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Person, Badge
from .forms import BadgeForm


def index(request):
    latest_person_list = Person.objects.order_by("-name")
    # template = loader.get_template('users/index.html')
    context = {"latest_person_list": latest_person_list}
    return render(request, "users/index.html", context)
    # return HttpResponse(template.render(context, request))


def user_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, "users/detail.html", {"person": person})


def badge_detail(request, person_id):
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
