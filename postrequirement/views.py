from django.shortcuts import render, redirect
from .models import Requirement

# Create your views here.
def requirement(request):
    return render(request, 'postrequirement/requirement.html')