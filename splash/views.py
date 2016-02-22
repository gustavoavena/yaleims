from django.shortcuts import render
from django.http import HttpResponse

import scores.models as Scores


def index(request):
	# return HttpResponse('Welcome to the Yale IMs!')
	colleges = Scores.ResidentialCollege.objects.all()
	podium = colleges[:3]
	context = {"colleges" : colleges, "podium" : podium, "positions" : [range(1, 13)]}
	print(podium[0].name)
	return render(request, 'index.html', context)

def create_college():
	pass