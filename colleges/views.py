from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def college_homepage(request):
	return HttpResponse('Colleges page!')