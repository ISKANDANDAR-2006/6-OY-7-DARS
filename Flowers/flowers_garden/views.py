
from django.shortcuts import render, get_object_or_404
from .models import Tur, Gul

def barcha_gullar(request):
    gullar = Gul.objects.all()
    return render(request, 'flowers/barcha_gullar.html', {'gullar': gullar})


def gullar_turi_bo_yicha(request, tur_id):
    turlar = get_object_or_404(Tur, id=tur_id)
    gullar = turlar.gullar.all()
    return render(request, 'flowers/gullar_turi_bo_yicha.html', {'gullar': gullar, 'tur': turlar})


def bitta_gul(request, gul_id):
    gul = get_object_or_404(Gul, id=gul_id)
    return render(request, 'flowers/bitta_gul.html', {'gul': gul})


def barcha_turlar(request):
    turlar = Tur.objects.all()
    return render(request, 'flowers/barcha_turlar.html', {'turlar': turlar})
