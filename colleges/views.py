from django.shortcuts import render, redirect
from django.http import HttpResponse

from scores.models import ResidentialCollege

# Create your views here.

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
	# return HttpResponse('Colleges page!')
	if request.method != 'GET':
		HttpResponse('Wrong method')
	else :
		if 'college' not in request.GET.keys():
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
		# return HttpResponse(College.get_name_display())

	return HttpResponse('Colleges page!')
