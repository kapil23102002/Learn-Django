from django.shortcuts import render
from course.models import Student
from .form  import LoginForm

# Create your views here.
def home(request):
    return render(request,  "index.html")

def django(request):
    return render(request,  "django.html")

def react(request):
    return render(request,  "react.html")


def nav(request): 
    return render(request,  "nav.html")

def studetails(request):
    stud = Student.objects.all()
    return render(request,  "studetails.html" , {'stu' :stud})

def showform(request):
    fm = LoginForm(auto_id=True, label_suffix=' ↔️', initial={'name': 'kapil', 'email': 'kapil@gmail.com'})
    fm.order_fields(field_order=['email', 'name'])
    return render(request,  "LoginForm.html" , {'form' :fm})