from django.shortcuts import render
from .settings import TEMPLATES
def index(request):
    print(TEMPLATES[0])
    return render(request, 'index.html', {})