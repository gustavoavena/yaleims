from django import forms
MAX_LENGTH = 50


COLLEGES_CHOICES = (
	('BK', 'Berkeley College'),
	('BR', 'Branford College'),
	('CC', 'Calhoun College'),
	('DC', 'Davenport College'),
	('ES', 'Ezra Stile College'),
	('JE', 'Jonathan Edwards College'),
	('MC', 'Morse College'),
	('PC', 'Pierson College'),
	('SM', 'Silliman College'),
	('SY', 'Saybrook College'),
	('TC', 'Trumbull College'),
	('TD', 'Timothy Dwight College'),
)


#form to register users.
class RegisterForm(forms.Form):
    full_name = forms.CharField(label='Name', max_length=MAX_LENGTH, required=True, widget=forms.TextInput(attrs={'class' : "form-control", "placeholder": "Full Name", 'name' : 'full_name', 'type': 'text'}))
    username = forms.CharField(label='Username', max_length=MAX_LENGTH, required=True, widget=forms.TextInput(attrs={'class' : "form-control", "placeholder": "Username", 'name' : 'username', 'type': 'text'}))
    password = forms.CharField(label="Password", max_length=MAX_LENGTH, required=True, widget=forms.PasswordInput(attrs={'class' : "form-control", "placeholder": "Password", 'name' : 'password', 'type':'password'}))
    password_confirmation = forms.CharField(label="Passoword Confirmation", max_length=MAX_LENGTH, required=True, widget=forms.PasswordInput(attrs={'class' : "form-control", "placeholder": "Password Confirmation", 'name' : 'password_confirmation', 'type':'password'}))
    isMaster = forms.BooleanField(required=False)
    residentialCollege = forms.ChoiceField(choices=COLLEGES_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'name': 'residentialCollege', 'id':'residentialCollege'}))


#form to log in users.
class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=MAX_LENGTH, required=True, widget=forms.TextInput(attrs={'class' : "form-control", "placeholder": "Username", 'name' : 'username', 'type': 'text'}))
	password = forms.CharField(label="password", max_length=MAX_LENGTH, widget=forms.PasswordInput(attrs={'class' : "form-control", "placeholder": "Password", 'name' : 'password', 'type':'password'}), required=True)