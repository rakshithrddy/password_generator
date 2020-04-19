from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    string = 'abcdefghijklmnopqurstuvwzyz'
    special_char = "!@#$%^&*()"
    numbers = '1234567890'
    characters = list(string)
    length = int(request.GET.get(key='length'))

    if request.GET.get(key='uppercase'):
        characters.extend(list(string.upper()))
    if request.GET.get(key='special'):
        characters.extend(list(special_char))
    if request.GET.get(key='numbers'):
        characters.extend(list(numbers))

    passwd = ''
    for i in range(length):
        passwd += random.choice(characters)
    return render(request, 'generator/password.html', {'password': passwd})


def about(request):
    return render(request, 'generator/about.html')