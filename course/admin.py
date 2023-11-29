from django.contrib import admin
from course.models import Student, Page

@admin.register(Student)  # this is decorator
class StudentAdmin(admin.ModelAdmin):
    list_display= ['stuid', 'stuname', 'stuemail', 'stupass']

# Register your models here.
# admin.site.register(Student, StudentAdmin) ---- we use decorator uper side


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display= ['page_name', 'page_details', 'page_publish_date', 'user']


