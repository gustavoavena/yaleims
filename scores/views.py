from django.shortcuts import render, redirect
from django.http import HttpResponse
import scores.forms as ScoresForms
import scores.models as ScoresModels
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

SPORTS = (("men_socer", 'Men Soccer'),("women_soccer", 'Women Soccer'),("men_footbal", 'Men Footbal'),("women_footbal", 'Women Football'),)



@login_required(login_url='/users/login')
def input_scores(request):
	if request.method == 'GET':
		InputScoresForm = ScoresForms.InputScores
		context = {'InputScoresForm' : InputScoresForm}
		return render(request, 'input_scores.html', context)
	
	elif request.method == 'POST':
		form = ScoresForms.InputScores(data=request.POST)
		if form.is_valid():
			formData = form.cleaned_data
			sport = ScoresModels.Sport.objects.filter(sport=formData['sport'])
			if not sport:
				print('Creating new sport in DB: ' + formData['sport'])
				sport = ScoresModels.Sport(sport=formData['sport'])
				sport.save()
			else:
				sport = sport[0]

			match = ScoresModels.Match(sport=sport, date=formData['date'])
			match.save()
			for col in [elem for elem in formData.keys() if elem != 'sport' and elem != 'date']:
				if formData[col] != None:
					try:
						c = ScoresModels.ResidentialCollege.objects.get(name=col)
					except:
						print('Could not find college: ' + col)
						messages.add_message(request, messages.ERROR, 'Could not find college: ' + str(col))
						return redirect('/')
					point = ScoresModels.Points(college=c, match=match, points=int(formData[col]))
					point.save()
					c.total += point.points
					c.save()

			messages.add_message(request, messages.SUCCESS, 'Scores added successfully.')	
			return redirect('/')
		else:
			for msg in form.errors.as_data().items():
				messages.add_message(request, messages.ERROR, str(msg[0]) + ': ' + str(msg[1]))
			return redirect('/')
	else:
		return HttpResponse('Error inputing scores.')	


@login_required(login_url='/users/login')
def remove_scores(request):
	if 'match_id' not in request.GET.keys(): #render the remove_scores_view
		matches = ScoresModels.Match.objects.all()
		context = {'matches' : matches}
		return render(request, 'remove_scores.html', context)
	else:
		id = request.GET['match_id']
		try:
			match = ScoresModels.Match.objects.get(id=id)
		except:
			messages.add_message(request, messages.ERROR, 'Error fetching this match from the database.')
			return redirect('/')

		match.delete()
		messages.add_message(request, messages.SUCCESS, 'Match removed successfully.')
		return redirect('/')
