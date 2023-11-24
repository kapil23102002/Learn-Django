from django import forms
from django.core import validators
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# -----------------------This is Model Form------------------------------

class LoginForm(forms.ModelForm):
    stuname = forms.CharField(max_length=20, min_length=4) # extra validation in model form
    class Meta:
        model = Student
        fields = ['stuid', 'stuname', 'stuemail', 'stupass']
        # fields = '__all__' sari fields show hogi jitni models me hai      
        # exclude = ['name'] is field ko chod kr sari fields show hogi

        labels = {'stuid': 'Roll No.', 'stuname':'Name', 'stuemail': 'Email', 'stupass':'Password'}
        widgets = {'stupass': forms.PasswordInput,'stuname':forms.TextInput}
        # error_messages = {'name': {'required':'Roll No. Likhna hai '}, 'stuname':{'required':'Name Likhna hai '}, 'stuemail': {'required':'Email Likhna hai '}, 'stupass':{'required':'Password Likhna hai '}}

# ---------Model Inheritance------------------
# padh liya geeky show se (70th)  video

# -------auth user with more inputs----------------------------

class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
        labels = {'email':'Email'}


# # ---------------This is Form Api---------------------------

# # ---------custom validation with built in method -------
# # def start_with_k(value):
# # 	if value[0] != 'k':
# # 		raise forms.ValidationError('Please start with K')
# # validators=[start_with_k] , (ye kisi bhi field me laga skte hai validation ke liye )

# class LoginForm(forms.Form):
# 	id = forms.IntegerField(error_messages=  {'required':'Enter yor Id'})
# 	name = forms.CharField( error_messages=  {'required':'Enter yor Name'}, widget=forms.Textarea)
# 	email = forms.EmailField(error_messages=  {'required':'Enter yor Email'})
# 	password = forms.CharField(error_messages=  {'required':'Enter yor Password'})

# # ---------proper validation -------
# 	def clean(self):
# 		cleaned_data = super().clean()
# 		valname = self.cleaned_data['name']
# 		valemail = self.cleaned_data['email']
		
# 		if len(valname) < 4:
# 			raise forms.ValidationError('Name should be more than 4 characters..')
		
# 		if len(valemail) < 10:
# 			raise forms.ValidationError('Email should be more than 10 characters..')
		
