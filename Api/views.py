from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from requests import Response
from rest_framework import viewsets

# Create your views here.
from rest_framework.views import APIView

from Api.models import Institution, Faculter, Option, Expert, Utilisateur

from Api.serializers import Institutionserializer, faculterserializer, Optionserializer, Expertserializer, \
    Utilisateurserializer


class InstitutionView(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = Institutionserializer


class FaculterView(viewsets.ModelViewSet):
    queryset = Faculter.objects.all()
    serializer_class = faculterserializer


class OptionView(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = Optionserializer


class ExpertView(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = Expertserializer


class UtilisateurView(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = Utilisateurserializer






def polls_list(request):
    MAX_OBJECTS = 20
    polls = Institution.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("nom_institution", "adresse", "telephone", "email", "fondateur", "date"))}
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Institution, pk=pk)
    data = {"results": { "Nom Institution": poll.nom_institution, "adresse": poll.adresse, "Telephone": poll.telephone, "Email": poll.email, "Fondateur": poll.fondateur, "Date": poll.date}}
    return JsonResponse(data)



