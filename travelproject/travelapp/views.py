from django.http import HttpResponse
from django.shortcuts import render
from .models import placce


# Create your views here.
def demo(request):
    obj = placce.objects.all()
    return render(request, 'index.html', {'result': obj})
