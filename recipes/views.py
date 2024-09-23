from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipes/pages/home.html', context= {'author_name': 'Ed',})

def teste_aninhamento(request):
    return HttpResponse('Teste do aninhamento 2')