from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from scores.models import ResidentialCollege


def get_score_by_sport(points):
	scores = {}
	for p in points:
		sport = p.match.sport.sport
		print(sport)
		if sport not in scores.keys():
			scores[sport] = p.points
		else:
			scores[sport] += p.points

	return scores

def college_homepage(request):
	if request.method != 'GET':
		messages.add_message(request, messages.ERROR, 'You did something wrong... To access a college\'s homepage, click its icon.')
		return redirect('/')
	else :
		if 'college' not in request.GET.keys():
			messages.add_message(request, messages.ERROR, 'You did something wrong... To access a college\'s homepage, click its icon.')
			return redirect('/')
		college = request.GET['college']
		College = ResidentialCollege.objects.get(name=college)
		points = College.points.all()
		scores = get_score_by_sport(points)
		print(scores)
		ordered_scores = []
		for s in sorted(scores, key=scores.__getitem__, reverse=True):
			ordered_scores.append((s, scores[s]))
		print(ordered_scores)
		context = {'college' : College, 'scores' : ordered_scores}
		return render(request, 'colleges_view.html', context)

