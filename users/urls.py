from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),

    path("user/new/", views.person_form, name="add_person"),
    path("user/<int:person_id>/", views.person_detail, name="person_detail"),
    path("user/<int:person_id>/edit/", views.person_form, name="edit_person"),

    path("badge/new/", views.badge_form_view, name="add_badge"),
    path("badge/<int:badge_id>/edit/", views.badge_form_view, name="edit_badge"),
    path("badge/<int:badge_id>/", views.badge_detail, name="badge_detail"),
]
