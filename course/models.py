from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=70)

    # def __str__ (self): 
    #     return self.stuname

    def get_absolute_url(self):
        return reverse("Showdata", kwargs = {"pk": self.pk})       
    
class Page(models.Model):

# --------------One To One Relationship -----------------
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True) # if user will delete then page will automatic delete
    # user = models.OneToOneField(User, on_delete = models.PROTECT, primary_key=True) # if user will delete then page will automatic delete
    # user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True , limit_choices_to={'is_staff': True  }) # Only staff user can create a page 


# --------------Many To One Relationship -----------------
    # user = models.ForeignKey(User, on_delete = models.CASCADE) # if user will delete then page will automatic delete
    # user = models.ForeignKey(User, on_delete = models.PROTECT, primary_key=True) # if user will delete then page will automatic delete
    # user = models.ForeignKey(User, on_delete = models.CASCADE, primary_key=True , limit_choices_to={'is_staff': True  }) # Only staff user can create a page 


# --------------Many To One Relationship -----------------
    # user = models.ManyToManyField(User)
    page_name = models.CharField(max_length=30)
    page_details = models.TextField()
    page_publish_date = models.DateField()

    
# For Pagination ----

class Pagination(models.Model):
    title = models.CharField(max_length=70)
    desc = models.TextField(max_length=700)
    publish_date = models.DateTimeField()

    def __str__ (self): 
        return self.title