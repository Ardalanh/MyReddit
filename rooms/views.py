from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

def home(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})
# Create your views here.
