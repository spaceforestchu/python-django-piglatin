from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'home.html')

def translate(request):
    text = request.GET['text']

    translation = ''
    for word in text.split():
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            translation += word
            translation += 'yay '
        else:
            translation += word[1:]

            translation += word[0]

            translation += 'ay '

    return render(request, 'translate.html', {'original' : text, 'translation': translation})

def about(request):
    return render(request, 'about.html')