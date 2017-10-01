import logging
import requests
from django.utils import timezone
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Line
from .models import Log

logger = logging.getLogger(__name__)


def index(request):
    return JsonResponse({"foo": "bar"})


def getstatus(request):
    response = requests.get("http://www.viaquatro.com.br/generic/Main/LineStatus")
    return JsonResponse(response.json())


def update_lines(request):
    # Make request at via 4 api
    req = requests.get("http://www.viaquatro.com.br/generic/Main/LineStatus")
    # get data as json
    data = req.json()

    # The response variable
    response = []

    # Get the via 4 status
    _line = {
        'number': 4,
        'color': "Amarela",
        'name': "Linha 4 - Amarela"
    }
    _save_line(_line)
    _log(_line, data['CurrentLineStatus']['Status'], data['CurrentLineStatus']['FinalDescription'])

    # Get metro lines info
    for obj in data['StatusMetro']['ListLineStatus']:
        _line = {
            'number': obj['Id'],
            'color': obj['Color'],
            'name': obj['Line']
        }
        _save_line(_line)
        _log(_line, obj['StatusMetro'], obj['Description'])

    return JsonResponse({
        'status': "ok",
        'message': "Lines Updated Successfully"
    })


# PRIVATE FUNCTION
def _save_line(_line):
    line = Line.objects.filter(number=_line['number'])
    logger.error(line.first().color)
    if line.exists():
        logger.error("Saving a new line 1")
        line.update(
            number=_line['number'], color=_line['color'],
            name=_line['name'],
            updated_at=timezone.now()
        )
    else:
        logger.error("Saving a new line")
        Line(
            number=_line['number'],
            color=_line['color'],
            name=_line['name']
        ).save()


def _log(_line, _status, _description):
    # Get the line
    line = Line.objects.filter(number=_line['number']).first()
    # Get the last log for the line
    last_log = Log.objects.filter(line_id=line.id).last()
    # Verify if status changed or the log does not exist
    if (not last_log) or (_status != last_log.status):
        Log(
            line_id=line.id,
            status=_status,
            description=_description
        ).save()
    else:
        Log.objects.filter(id=last_log.id).update(
            updated_at=timezone.now()
        )
