from django.shortcuts import render
from course.models import Student
from .form  import LoginForm
from django.http import HttpResponseRedirect

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
    if request.method == 'POST':
        fm = LoginForm(request.POST,  auto_id=True, label_suffix=' ↔️', initial={'name': 'kapil', 'email': 'kapil@gmail.com'})
        if fm.is_valid():
            i =  fm.cleaned_data['id']
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ps = fm.cleaned_data['password']
            reg = Student(stuname = nm, stuemail = em , stuid = i , stupass = ps)
            reg.save()
            fm = LoginForm()
            return HttpResponseRedirect('/cor/success/')
    else:
        fm = LoginForm()
    fm.order_fields(field_order=['email', 'name'])
    return render(request,  "LoginForm.html" , {'form' :fm})

def success(request):
    return render(request, 'success.html')