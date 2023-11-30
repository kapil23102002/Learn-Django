from django.urls import path
from course import views

urlpatterns = [
    path('', views.home),
    path('django/', views.django , name="django"),
    path('react/', views.react , name="react"),
    path('nav/', views.home , name="nav"),
    path('stu/', views.studetails , name="studetails"),
    path('form/', views.showform , name="showform"),
    path('success/', views.success ),
    path('details/<int:pk>/', views.showdetails , name="showdata"),
    path('bsignup/', views.bsignup , name="bsignup"),
    path('signup/', views.signup , name="signup"),
    path('login/', views.login , name="login"),
    path('profile/', views.profile , name='profile'),
    path('logout/', views.logout , name="logout"),
    path('changepass/', views.changepass , name="changepass"),
    path('editprofile/', views.editprofile , name="editprofile"),
    path('userinfo/<int:id>', views.userinfo , name="userinfo"),
    path('sessions/', views.sessions , name='sessions'),
    path('set/', views.setsession , name='setsession'),
    path('get/', views.getsession , name='getsession'),
    path('del/', views.delsession , name='delsession'),
    path('middleware/', views.middleware ),
    path('classview/', views.classview.as_view() , name = 'classview'),
    path('classform/', views.classform.as_view() , name = 'classform'),
    path('home/', views.RedirectView.as_view(url = '/cor/classform') , name = 'home'),
    path('Showdata/', views.ShowList.as_view() , name = 'showlist'),
    path('Showdata/<int:pk>', views.ShowData.as_view() , name = 'Showdata'),
    path('genricform/', views.GenricForm.as_view() , name = 'genricform'),
    path('thankyouform/', views.ThankyouForm.as_view() , name = 'thankyouform'),
    path('genricformsaved/', views.GenricFormSaved.as_view() , name = 'genricformsaved'),
    path('updatedata/<int:pk>', views.UpdateData.as_view() , name = 'updatedata'),
    path('deletedata/<int:pk>', views.DeleteData.as_view() , name = 'deletedata'),


    








    

    

    

    











]
