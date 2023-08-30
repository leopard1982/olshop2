from django.shortcuts import render

from administrasi.serializersnya import serialSearchKeyword

from administrasi.models import searchKeyword

from rest_framework.decorators import api_view

from rest_framework.response import Response

# Create your views here.
def dashboard(request):
    return render(request,'base.html')
