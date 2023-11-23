from django import forms
from django.core import validators

# custom validation with built in method -------

def start_with_k(value):
	if value[0] != 'k':
		raise forms.ValidationError('Please start with K')

class LoginForm(forms.Form):
	name = forms.CharField(validators=[start_with_k], error_messages=  {'required':'Enter yor Name'}, widget=forms.Textarea)
	email = forms.EmailField(error_messages=  {'required':'Enter yor Email'})

# proper validation -------
	def clean(self):
		# cleaned_data = super().clean()
		valname = self.cleaned_data['name']
		valemail = self.cleaned_data['email']
		
		if len(valname) < 4:
			raise forms.ValidationError('Name should be more than 4 characters..')
		
		if len(valemail) < 10:
			raise forms.ValidationError('Email should be more than 10 characters..')
		
