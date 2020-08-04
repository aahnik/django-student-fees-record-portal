from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> you are at student_management index </h1>")
