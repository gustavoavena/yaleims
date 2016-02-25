from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
import users.forms
import users.models
import scores.models
# import users.models
import re as regex


#I used Django's built-in authentication modules. They are simple and work great.

#this function is responsible for registering users. It gets a register form from the POST request, handles the data, saves the users to the db and logs the user in.
# @login_required(login_url='/')
@staff_member_required(login_url='/users/login') #this way, only staff (or master) users, can register users.
def register(request):
	if request.method == 'GET':
		registerForm = users.forms.RegisterForm()
		context = {'registerForm' : registerForm}
		return render(request, 'register.html', context)
	elif request.method != 'POST':
		print('Wrong request method for registering.') #for debugging.
		return HttpResponse('Request Error')
	else:
		form = users.forms.RegisterForm(request.POST) #creates a RegisterForm object from the form in the POST request. All of the form classes I use are derived from Django's Form class.
		print('New user registering. Fetching form data...')
		if form.is_valid(): #checks if the form is valid and sets the cleaned_data attribute with the form data in a dictionary format.
			formData = form.cleaned_data
			if formData['password'] != formData['password_confirmation']: #checks if password and password confirmation match.
				return redirect('/', {'errors': 'Password and password confirmation dont match.'})
			try: #tries to create a new user (user object) and save it to the db. It saves the new object automatically and returns an error if something goes wrong.
				if formData['isMaster']:
					user = User.objects.create_user(username=formData['username'], password=formData['password'], first_name=formData['full_name'], is_staff=True)
				else:
					user = User.objects.create_user(username=formData['username'], password=formData['password'], first_name=formData['full_name'], is_staff=False)
			except Exception, e: #if there is an error, I check it to see if it matches any error that should be informed to the testing script (like invalid email or duplicate email).
				print('error creating user:')
				# print(e) #for debugging 
				errors = "?errors=" + str(e)
				return redirect('/' + errors)
			
			user = authenticate(username=formData['username'], password=formData['password']) #before using the login function to log a user in, 
			#the authenticate function needs to be called to set some attributes in the user object and allow it to be logged in.
			login(request, user)
			print('New user registered! User: ' + user.username + '. Logging user in...') #for debugging
			return redirect('/')
		else:
			# print(form.errors.as_data()) #for debugging.
			errors = '?errors=' + str(form.errors.as_data()[0])
			return redirect('/' + errors)
	


def login_user(request):
	if request.method == 'GET':
		loginForm = users.forms.LoginForm()
		context = {'loginForm' : loginForm}
		return render(request, 'login.html', context)
	elif request.method != 'POST':
		return HttpResponse('Request Error')
	else:
		form = users.forms.LoginForm(request.POST) #same as the other functions that process forms.
		if form.is_valid():
			formData = form.cleaned_data
			user = authenticate(username=formData['username'], password=formData['password'])
			if user is not None: #if there is an user in the db and the password matches, logs the user in.
				print('Valid user!!')
				login(request, user)
				return redirect('/')
			else: 
				return redirect('/?errors=Invalid+password+or+email')
			
		else:
			errors = '?errors=' + str(form.errors.as_data()[0])
			return redirect('/' + errors)


@login_required(login_url='/users/login')
def logout_user(request): #logs out the user by calling django's logout function.
	print('User logged out!')
	logout(request)
	return redirect('/')

