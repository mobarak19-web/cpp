# from django.contrib import admin
# from .models import students


# class Adminstudents(admin.ModelAdmin):
#     list_display = ('id', 'name', 'email','age', 'course', 'semester', 'created_at')


# admin.site.register(students, Adminstudents)


# models registration filed
from django.contrib import admin
from .models import student
from .models import teacher

class Adminstudent(admin.ModelAdmin):
    list_display=('id','name','email','course','semester','age','created_at')

admin.site.register(student)

class Adminteacher(admin.ModelAdmin):
    list_display=('id','name','email','department','designation','age','created_at')

admin.site.register(teacher)

