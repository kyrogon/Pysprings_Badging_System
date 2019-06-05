from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:person_id>/", views.detail, name="detail"),
    path("<int:person_id>/badge/", views.badge, name="badge"),
    # path("<int:person_id>/add_badge/", views.add_badge, name="add_badge"),
    path("add_person/", views.add_person, name="add_person"),

    path('badges/', views.badge_list, name='badge_list'),
    path('badges/add/', views.badge_form, name='add_badge'),
    path('badge/<int:badge_id>/edit/', views.badge_form, name='edit_badge'),
    path('badge/<int:badge_id>/', views.badge_detail, name='badge_detail'),
]
