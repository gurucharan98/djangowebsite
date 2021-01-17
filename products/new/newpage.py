# this is a new page program created by me

from django.http import HttpResponse
from django.shortcuts import render


def new_page(request):
    return HttpResponse('this is my new page')