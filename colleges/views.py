from django.shortcuts import render, redirect
from django.http import HttpResponse

from scores.models import ResidentialCollege

# Create your views here.


def college_homepage(request):
	# return HttpResponse('Colleges page!')
	if request.method != 'GET':
		HttpResponse('Wrong method')
	else :
		if 'college' not in request.GET.keys():
			return redirect('/')
		college = request.GET['college']
		College = ResidentialCollege.objects.get(name=college)
		context = {'college' : College}
		return render(request, 'colleges_view.html', context)
		# return HttpResponse(College.get_name_display())

	return HttpResponse('Colleges page!')
