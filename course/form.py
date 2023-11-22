from django import forms

class LoginForm(forms.Form):
        name = forms.CharField(error_messages=  {'required':'Enter yor Name'}, widget=forms.Textarea)
        email = forms.EmailField(error_messages=  {'required':'Enter yor Email'})
