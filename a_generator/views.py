from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def Password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('~`!@#$%^&*()"_:?/;,.[]`'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length'))
    thepassword = ''

    for _ in range(length):
            thepassword += random.choice(characters)

    return render(request, 'Password.html', {'password': thepassword})
