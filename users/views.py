from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Person, Badge
from . import forms


# Create your views here.
def index(request):
    latest_person_list = Person.objects.order_by("-name")
    # template = loader.get_template('users/index.html')
    context = {"latest_person_list": latest_person_list}
    return render(request, "users/index.html", context)


def person_detail(request, person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, "users/user_detail.html", {"person": person})


def badge_detail(request, badge_id):
    badge = get_object_or_404(Badge, pk=badge_id)
    return render(request, "users/badge_detail.html", {"badge": badge})


def person_form(request, person_id=None):
    context = {
        'error_message': None,
        'page_form':     None,
    }

    if person_id:
        user = get_object_or_404(Person, id=person_id)
        form = forms.UserForm(instance=user)
    else:
        user = None
        form = forms.UserForm()

    if request.method == 'POST':
        form = forms.UserForm(request.POST, instance=user)
        if form.is_valid():
            instance = form.save()
            return redirect('users:person_detail', person_id=instance.id)

    context['page_form'] = form

    return render(
        request,
        'users/user_form.html',
        context=context
    )


def badge_form_view(request, badge_id=None):
    context = {
        'error_message': None,
        'page_form':     None,
    }

    if badge_id:
        badge = get_object_or_404(Badge, id=badge_id)
        form = forms.BadgeForm(instance=badge)
    else:
        badge = None
        form = forms.BadgeForm()

    if request.method == 'POST':
        form = forms.BadgeForm(request.POST, instance=badge)
        if form.is_valid():
            instance = form.save()
            return redirect('users:badge_detail', badge_id=instance.id)

    context['page_form'] = form

    return render(
        request,
        "users/badge_form.html",
        context,
    )
