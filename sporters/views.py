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

@csrf_exempt
def result_player(request, idSpeler, matchCode):
    gekregen_Speler = speler.objects.get(pk = idSpeler)
    gekregen_MatchCode = match_punten.objects.get(pk = matchCode)
    MD_speler = model_to_dict(gekregen_Speler)
    MD_speler["id"] = model_to_dict(gekregen_MatchCode["punten"])
    return JsonResponse(MD_speler)


def punten_speler(request, idSpeler):
    gekregen_speler = speler.objects.get(pk = idSpeler)
    gekregen_match = match_punten.objects.all.value()
