from django.shortcuts import render
from .models import Games
from django.http import HttpResponse
from django.core.serializers import serialize

def index(request):
    games = Games.objects.all()
    return render(request, 'homepage/index.html', { 'games': games })

def games(request):
    games = serialize('json', Games.objects.all())
    return HttpResponse(games, content_type='application/json')