from django import forms
from functools import partial

SPORTS = (("men_socer", 'Men Soccer'),("women_soccer", 'Women Soccer'),("men_footbal", 'Men Footbal'),("women_footbal", 'Women Football'),)

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


#This is the create task form.
class InputScores(forms.Form):
	sport = forms.ChoiceField(choices=SPORTS, widget=forms.Select(attrs={'class': 'form-control', 'name': 'sport', 'id':'sport'}))
	date = forms.DateField(widget=DateInput())
	BK = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'BK', 'type':'number'}))
	BR = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'BR', 'type':'number'}))
	CC = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'CC', 'type':'number'}))
	DC = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'DC', 'type':'number'}))
	ES = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'ES', 'type':'number'}))
	JE = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'JE', 'type':'number'}))
	MC = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'MC', 'type':'number'}))
	PC = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'PC', 'type':'number'}))
	SM = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'SM', 'type':'number'}))
	SY = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'SY', 'type':'number'}))
	TC = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'TC', 'type':'number'}))
	TD = forms.IntegerField(required=False, widget=forms.TextInput(attrs={'class' : "form-control", 'name' : 'TD', 'type':'number'}))