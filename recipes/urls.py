from django.urls import path
from recipes.views import home, teste_aninhamento

urlpatterns = [
    path('', home), #Home
    path('aninhamento/', teste_aninhamento),
    path('aninhamento1/aninhamento2', teste_aninhamento),
]