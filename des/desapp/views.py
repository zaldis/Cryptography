from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Main page dor des algorithm!")
