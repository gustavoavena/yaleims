from django.shortcuts import render
from django.http import HttpResponse

import scores.models as Scores


def index(request):
	# return HttpResponse('Welcome to the Yale IMs!')
	if 'errors' in request.GET.keys():
		errors = request.GET['errors']
	else:
		errors = None
	colleges = Scores.ResidentialCollege.objects.all()
	print(colleges)
	colleges = colleges.order_by('total')
	podium = colleges[:3]
	context = {"colleges" : colleges, "podium" : podium, "positions" : [range(1, 13)], "errors" : errors}
	# print(podium[0].name)
	return render(request, 'index.html', context)

def create_college():
	pass