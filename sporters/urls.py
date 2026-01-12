from django.urls import path
from . import views

urlpatterns = [
    path("", views.werkt),
    path("addPlayer/", views.add_speler),
    path("onePlayer/<int:id>", views.speler_id),
    path("AllPlayers/", views.all_Spelers),
    path("addResult/", views.add_result)
]