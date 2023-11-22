from django.contrib import admin
from course.models import Student

@admin.register(Student)  # this is decorator
class StudentAdmin(admin.ModelAdmin):
    list_display= ('stuid', 'stuname', 'stuemail')

# Register your models here.
# admin.site.register(Student, StudentAdmin) ---- we use decorator uper side