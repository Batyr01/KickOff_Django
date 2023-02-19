from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    players = Players.objects.all()
    return render(request, 'website/index.html', {'players': players,'title': 'Index Page  '})

def about(request):
    return render(request, 'website/about.html', {'title': 'About Players'})


def pagenotfound(request, exception):
    return HttpResponseNotFound('<h1>Page Not Found</h1>')


def accessforbiden(request, exception):
    return HttpResponseNotFound('<h1>Access forbidden</h1>')


def servererror(request, exception):
    return HttpResponseNotFound('<h1>Error Server</h1>')


def error(request, exception):
    return HttpResponseNotFound('<h1>Error</h1>')
