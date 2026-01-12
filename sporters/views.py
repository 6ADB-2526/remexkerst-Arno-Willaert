from django.shortcuts import render
from .models import speler, match_punten
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.

def werkt(request):
    return HttpResponse("het werkt")

@csrf_exempt
def add_speler(request):
    post_data =  json.loads(request.body.decode('utf-8'))

    nieuwe_speler = speler()
    nieuwe_speler.naam = post_data['naam']
    nieuwe_speler.voornaam = post_data['voornaam']
    nieuwe_speler.email = post_data['email']

    nieuwe_speler.save()

    return HttpResponse("nieuwe speler is aangemaakt")

def speler_id(request, id):
    gekregen_speler = speler.objects.get(pk = id)

    return JsonResponse(model_to_dict(gekregen_speler))

def all_Spelers(request):
    alle_spelers = speler.objects.all().values()

    return JsonResponse(list(alle_spelers), safe=False)


@csrf_exempt
def add_result(request):
    post_data =  json.loads(request.body.decode('utf-8'))

    nieuw_Resultaat = match_punten()
    nieuw_Resultaat.nummerSpeler = post_data['nummerSpeler']
    nieuw_Resultaat.punten = post_data['punten']
    nieuw_Resultaat.matchCode = post_data['matchCode']

    nieuw_Resultaat.save()

    return HttpResponse("er is een nieuw resultaat aangemaakt")


def result_player(request, idSpeler, matchCode):
    