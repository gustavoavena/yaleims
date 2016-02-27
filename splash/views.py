from django.shortcuts import render
from django.http import HttpResponse

import scores.models as Scores


def index(request):
	colleges = Scores.ResidentialCollege.objects.all()
	colleges = colleges.order_by('total').reverse()
	podium = colleges[:3]
	context = {"colleges" : colleges, "podium" : podium, "positions" : [range(1, 13)]}
	return render(request, 'index.html', context)

