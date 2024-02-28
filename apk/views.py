from django.shortcuts import render
from django.shortcuts import render

def mi_vista(request):
    return render(request, 'template.html')
