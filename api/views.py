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


# FUNCTIONS
# Get current metro status
def getstatus(request):
    response = requests.get("http://www.viaquatro.com.br/generic/Main/LineStatus")
    return JsonResponse(response.json())


# Update Api database
def update(request):
    # Make request at via 4 api
    req = requests.get("http://www.viaquatro.com.br/generic/Main/LineStatus")
    # get data as json
    data = req.json()

    # Set the via 4
    _line = {
        'number': 4,
        'color': "Amarela",
        'name': "Linha 4 - Amarela"
    }
    # Save via 4
    _save_line(_line)

    # Log via 4 status
    _log(_line, data['CurrentLineStatus']['Status'], data['CurrentLineStatus']['FinalDescription'])

    # Get metro lines info
    for obj in data['StatusMetro']['ListLineStatus']:
        # Get line info
        _line = {
            'number': obj['Id'],
            'color': obj['Color'],
            'name': obj['Line']
        }
        # Save line
        _save_line(_line)
        # Log Line info
        _log(_line, obj['StatusMetro'], obj['Description'])

    # API endpoint Response
    return JsonResponse({
        'status': "ok",
        'message': "Lines Updated Successfully"
    })


# Get Log Endpoint
def logs(request):
    # results array
    results = []
    # Get line url param
    _line_number = request.GET.get('line', False)

    # verify if a line id was supplied
    if _line_number:
        # then, verify if the line exist
        line = Line.objects.filter(number=_line_number).first()
        if line:
            # if true, get the information about that line
            results.append({
                'line': _get_line(line),
                'logs': []
            })
            # Then, get the logs of that line
            for log in Log.objects.filter(line_id=line.id).order_by('-updated_at'):
                results[0]['logs'].append({
                    'log': _get_log(log)
                })
        else:
            # Else, the supplied line does not exist
            return JsonResponse({
                'status': "error",
                'message': "Line does not exist"
            })
    # Else, then no line was supplied, in this case return the logs of all lines
    else:
        # foreach line
        for i, line in enumerate(Line.objects.all().iterator()):
            # Get more information about that line
            results.append({
                'line': _get_line(line),
                'logs': []
            })
            # Then, get the logs of that line
            for log in Log.objects.filter(line_id=line.id).order_by('-updated_at'):
                results[i]['logs'].append({
                    'log': _get_log(log)
                })

    return JsonResponse(results, safe=False)


# PRIVATE FUNCTIONS
# Get the line info
def _get_line(line):
    return {
        'color': line.color,
        'number': line.number,
        'name': line.name
    }


# Get the log info
def _get_log(log):
    return {
        'status': log.status,
        'description': log.description,
        'updated_at': log.updated_at
    }


# Save the line in database
def _save_line(_line):
    # Verify if the supplied line exists
    line = Line.objects.filter(number=_line['number'])
    if line.exists():
        # In this case, update that line
        line.update(
            number=_line['number'], color=_line['color'],
            name=_line['name'],
            updated_at=timezone.localtime(timezone.now())
        )
    # Otherwise, save a new line
    else:
        Line(
            number=_line['number'],
            color=_line['color'],
            name=_line['name']
        ).save()


# Save the log in database
def _log(_line, _status, _description):
    # Get the line
    line = Line.objects.filter(number=_line['number']).first()
    # Get the last log for the line
    last_log = Log.objects.filter(line_id=line.id).last()

    # Verify if status changed or the log does not exist
    if (not last_log) or (_status != last_log.status):
        # In this case, save a new low
        Log(
            line_id=line.id,
            status=_status,
            description=_description
        ).save()
    else:
        # Otherwise, just update the updated_at field
        Log.objects.filter(id=last_log.id).update(
            updated_at=timezone.localtime(timezone.now())
        )