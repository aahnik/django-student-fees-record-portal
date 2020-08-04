from django.shortcuts import render
from django.utils import timezone


def index(request):
    now = timezone.now()
    context = {'now': now}
    return render(request, 'home/index', context)
