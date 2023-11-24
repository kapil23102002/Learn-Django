from django.shortcuts import render
from course.models import Student
from .form  import LoginForm, SignUpForm
from django.http import HttpResponseRedirect    
from django.contrib  import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


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
            i =  fm.cleaned_data['stuid']
            nm = fm.cleaned_data['stuname']
            em = fm.cleaned_data['stuemail']
            ps = fm.cleaned_data['stupass']
            reg = Student(stuname = nm, stuemail = em , stuid = i , stupass = ps)
            reg.save()
            fm = LoginForm()
            messages.success(request, 'Apka Form submit ho gaya hai ....')
            # messages.info(request, 'Apka Form submit ho raha hai ....')

            # return HttpResponseRedirect('/cor/success/')
    else:
        fm = LoginForm()
    fm.order_fields(field_order=['email', 'name'])
    return render(request,  "LoginForm.html" , {'form' :fm})

def success(request):
    return render(request, 'success.html')

def showdetails(request,pk):
    student = Student.objects.get(pk=pk)
    data={
        "roll":student.stuid,
        "name":student.stuname,
        "email":student.stuemail,
        "pass":student.stupass

    }
    return render(request, 'dynamicurl.html', data)

# ---User auth with built in method-----
def bsignup(request):
    if request.method == 'POST':
        frm = UserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm = UserCreationForm()
    return render(request, 'bsignup.html',{'form':frm} )

# --- add more inputs in User Registration method-----
            
def signup(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html',{'form':fm} )

# ----------User Login Form--------------

def login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():   
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/cor/profile/')
    else:
        fm = AuthenticationForm()   
    return render(request, 'login.html',{'form':fm} )

# ----show profile page -----------------

def profile(request):
    return render(request, 'profile.html')

# ----User Logout -----------------

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/cor/login/')
