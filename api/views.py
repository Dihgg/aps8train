import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    return JsonResponse({"foo": "bar"})


def getstatus(request):
    response = requests.get("http://www.viaquatro.com.br/generic/Main/LineStatus")
    return JsonResponse(response.json())
