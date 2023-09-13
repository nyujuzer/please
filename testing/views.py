from django.shortcuts import render
from .settings import TEMPLATES
def index(request):
    return render(request, 'index.html', {})