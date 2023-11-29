from django.shortcuts import render
from course.models import Student
from .form  import LoginForm, SignUpForm, UserProfile, AdminProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib  import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout,  update_session_auth_hash
from django.contrib.auth.models import User
from django.db.models import Avg, Sum, Min, Max, Count



# Create your views here.
def home(request):
        return render(request,  "index.html")

def django(request):
       return render(request,  "django.html")

def react(request):
      return render(request,  "react.html")


def nav(request): 
    return render(request,  "nav.html")

# -------------- Query Set Api ---------------
def studetails(request):
    # stud = Student.objects.all()  # Return all fields 
    # stud = Student.objects.filter(stuid = 101) # Return Match fields
    # stud = Student.objects.exclude(stuid = 101) # Return UnMatch fields
    # stud = Student.objects.order_by('stuid') # Return assending order by Id field
    # stud = Student.objects.order_by('-stuid') # Return desending order by Id field
    # stud = Student.objects.order_by('?') # Return Randomly  order
    # stud = Student.objects.order_by('stuid').reverse()[:5] # Return last 5 value by reverse order
    # stud = Student.objects.values('stuname', 'stuid') # Return Custom values  
        # it has more methods But this Time we are DONE------ 

# This Query Set Api Methods are NOT Return New Query Set

    # stud = Student.objects.get(pk = 1) # Return by Primary Key which have PK = 1 value 
    # stud = Student.objects.first() # Return First value 
    # stud = Student.objects.last() # Return Last value 
    # stud = Student.objects.latest('stuid') # Return Latest value 
    # stud = Student.objects.earliest('stuid') # Return Earliest value 
    # stud = Student.objects.create({pura data object me likhna hai}) # Return  and add new data 
    # stud = Student.objects.filter(pk= 1).update(stuname= 'akash') # Return Updated  value, shows in admin pannel
    # stud = Student.objects.get(pk = 2).delete() # Delete by Primary Key which have PK = 2 value 
    # stud = Student.objects.all().count() # Return Number of value in terminal
    # print(stud)
    #     # it has more methods But this Time we are DONE------ 

# Aggregation method in Query Set ApI------
    # stud = Student.objects.all().aggregate(Avg('stuid'))
    # stud = Student.objects.all().aggregate(Sum('stuid'))
    # stud = Student.objects.all().aggregate(Sum('stuid'))
    # stud = Student.objects.all().aggregate(Max('stuid'))
    # stud = Student.objects.all().aggregate(Min('stuid'))
    stud = Student.objects.all().aggregate(Count('stuid'))
    print(stud)


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

# -------Student Details with dynamic URL----------

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
    if not request.user.is_authenticated:   
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
    else:
        return HttpResponseRedirect('/cor/profile/')


# ----show profile page -----------------

def profile(request):
    if request.user.is_authenticated:   
        if request.user.is_superuser == True:
            fm = AdminProfile(instance = request.user)
            Users = User.objects.all()
            ip = request.session.get('IP')
        else:
            Users = None
            fm = UserProfile(instance = request.user)
            ip = request.session.get('IP')
        return render(request, 'profile.html', {'name': request.user, 'form':fm, 'Users' : Users, 'ip': ip})
    else:
        return HttpResponseRedirect('/cor/login/')


# ----User Logout -----------------

def logout(request):
    # if not request.user.is_authenticated:   
        auth_logout(request)
        return HttpResponseRedirect('/cor/login/')
    # else:
        # return HttpResponseRedirect('/cor/profile/')
        
# ------------User can Change Password -----------------

def changepass(request):  
    if request.user.is_authenticated:   

        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/cor/profile/')

        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'changepass.html',{'form':fm} )
    else:
        return HttpResponseRedirect('/cor/login/')


# ------------User can Edit their Profile ----------------

def editprofile(request):
    if request.user.is_authenticated:  
        if request.method == 'POST':
            fm = UserProfile(request.POST, instance = request.user) 
            if fm.is_valid():
                messages.success(request, 'Profile Updated Successfully')
                fm.save()
        else:
            fm = UserProfile(instance = request.user)
        return render(request, 'editprofile.html', {'name': request.user, 'form':fm})
    else:
        return HttpResponseRedirect('/cor/login/')

# ------- Admin can view Other Users Profile------------

def userinfo(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk= id)
        fm = AdminProfile(instance = pi)
        return render(request, 'userinfo.html', {'form':fm} )
    else:
        return HttpResponseRedirect('/cor/login/')

# --------Sessions and its Methods -------------

def sessions(request):
    return render(request, 'sessions_framework/sessions.html')

def setsession(request):
    request.session['name'] = 'kapil'
    # set expiry date----\
    request.session.set_expiry(20)
    return render(request, 'sessions_framework/setsession.html')

def getsession(request):
    if 'name' in request.session:
        name = request.session.get('name')
        keys = request.session.keys()
        items = request.session.items()
        request.session.setdefault('age', '24')
        request.session.modified = True
        # expiry information---
        print(request.session.get_session_cookie_age())
        print(request.session.get_expiry_age())
        print(request.session.get_expiry_date())
        print(request.session.get_expire_at_browser_close())      
        return render(request, 'sessions_framework/getsession.html', {'name':name,'keys': keys, 'items':items})
    else:
        return HttpResponse('Your Session has been Expired....!!!')    

def delsession(request):
    request.session.flush()
    # clear expired session---
    request.session.clear_expired()
    return render(request, 'sessions_framework/delsession.html')

# -----------MiddleWare -------------

def middleware(request):
    print('I am View')

    return HttpResponse('This is Middleware Page')

