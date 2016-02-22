from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def input_scores(request):
	return HttpResponse('This is the input scores page.')

def remove_scores(request):
	return HttpResponse('This is the remove scores page.')