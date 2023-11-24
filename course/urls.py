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
    path('profile/', views.profile ),
    path('logout/', views.logout , name="logout"),
    path('changepass/', views.changepass , name="changepass"),











]
