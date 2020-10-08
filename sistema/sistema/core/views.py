from django.shortcuts import render

def home(request):
    pagina_inicial = {}
    return render(request, 'pagina_inicial.html', pagina_inicial)
