from django.shortcuts import render, get_object_or_404
from .models import Palco, Dia, Concerto

def index_view(request):
    return render(request, 'festival/index.html')

def dias_view(request):
    dias = Dia.objects.prefetch_related('concertos').all()
    return render(request, 'festival/dias.html', {'dias': dias})

def palcos_view(request):
    palcos = Palco.objects.prefetch_related('concertos').all()
    return render(request, 'festival/palcos.html', {'palcos': palcos})

def concerto_view(request, id):
    concerto = get_object_or_404(Concerto, pk=id)
    return render(request, 'festival/concerto.html', {'concerto': concerto})