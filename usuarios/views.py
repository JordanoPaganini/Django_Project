from django.shortcuts import render, HttpResponse
from .models import *

def cadastar_vendedor(requets):
    return HttpResponse('Você acessou a url de cadastro de vendedor')