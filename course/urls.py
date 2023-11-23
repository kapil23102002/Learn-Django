from django.urls import path
from course import views

urlpatterns = [
    path('', views.home),
    path('django/', views.django , name="django"),
    path('react/', views.react , name="react"),
    path('nav/', views.home , name="nav"),
    path('stu/', views.studetails , name="studetails"),
    path('form/', views.showform , name="showform"),
    





]
