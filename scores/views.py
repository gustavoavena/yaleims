from django.shortcuts import render, redirect
from django.http import HttpResponse
import scores.forms as ScoresForms

# Create your views here.



def input_scores(request):
	if request.method == 'GET':
		InputScoresForm = ScoresForms.InputScores
		context = {'InputScoresForm' : InputScoresForm}
		return render(request, 'input_scores.html', context)
	# return HttpResponse('This is the input scores page.')

def remove_scores(request):
	return HttpResponse('This is the remove scores page.')