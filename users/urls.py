from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path("user/new/", views.add_person, name="add_person"),
    path("user/<int:person_id>/", views.person_detail, name="person_detail"),
    path("badge/new/", views.add_badge, name="add_badge"),
    path("badge/<int:badge_id>/", views.badge_detail, name="badge_detail"),
]
