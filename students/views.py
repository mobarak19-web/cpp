from django.shortcuts import render, redirect

from SMS_Project.settings import EMAIL_HOST_USER # pyright: ignore[reportMissingModuleSource]
from .models import student,teacher
from .forms import studentForm, teacherForm
from django .contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .forms import UserRegistrationForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django .http import HttpResponse
import random
from django.core.mail import send_mail
from django.conf import settings
# from SMS_PROJECT.settings import EMAIL_HOST_USER
from .forms import *
from django.contrib.auth import update_session_auth_hash


def homepage(request):
     Students = student.objects.all()
     context={
          'student': Students
      }
     return render(request, 'home.html', context)
     # if request.method =="POST":
     
     


       #  list function...

# student list 

def student_list(request):
    students = student.objects.all()
    content={
        'students': students
    }
    return render(request, 'student_list.html', content)

#teacher list

def teacher_list(request):
    teachers = teacher.objects.all()
    content={
        'teachers': teachers
    }
    return render(request, 'teacher_list.html', content)

      #add function ...

# Add_ student 

def add_student(request):
    if request. method =="POST":
        form=studentForm(request.POST)
        if form.is_valid():
            form. save()
            return redirect("student_list")

    else:
           form = studentForm()
         
    return render(request, 'add_student.html', {'form': form})

#Add- teacher item 

def add_teacher(request):
    if request. method =="POST":
        form=teacherForm(request.POST)
        if form.is_valid():
            form. save()
            return redirect("teacher_list")

    else:
           form = teacherForm()
         
    return render(request, 'add_teacher.html', {'form': form})


         #edit function...


#teacher item edit...
def edit_teacher(request,id):
     Tchr = teacher.objects.get(id=id)
     if request.method =='POST':
          form = teacherForm(request.POST , instance=Tchr)
          if form.is_valid():
               form.save()
               return redirect('teacher_list')
          
     else:
          form = teacherForm(instance= Tchr)
     return render(request,'add_teacher.html',{'form':form})


# student item edit  
def edit_student(request, id):
     Std = student.objects.get(id=id)
     if request.method == 'POST':
          form = studentForm(request.POST, instance=Std)
          if form.is_valid():
               form.save()
               return redirect('student_list')
          
     else:
          form = studentForm(instance= Std)
     return render(request, 'add_student.html', {'form':form})


        #Delete functiion

#teacher item, delete ......
def delete_teacher(request, id):
     Std = teacher.objects.get(id=id)
     Std.delete()
     return redirect('teacher_list')

   
#student item delete 
def delete_student(request, id):
     Std = student.objects.get(id=id)
     Std.delete()
     return redirect('student_list')
   
        
#regitration form login,,,  logout,,,,update,,,,, profile,,,

#RegistrationForm 
def register_user(request):
    
     if request.method =='POST':
          form = UserRegistrationForm(request.POST)
          if form.is_valid():
               user = form.save()
               login(request,user)
               #role r edirect now 
               if hasattr(user, 'profile') and user.profile.role == 'teacher':
                    return redirect('teacher_list')
               return redirect('student_list')
          
     else:
          form = UserRegistrationForm()
     return render(request, 'register.html', {'form' : form})


# login view
# login view
def login_user(request):
     if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None: 
                  login(request, user)  # ঠিক করা হয়েছে: (request, user)
                # Role redirect
                  if hasattr(user, 'profile') and user.profile.role == 'teacher':
                       return redirect('teacher_list')
                  return redirect('student_list')
     else:
        form = AuthenticationForm()

    # Bootstrap class dynamic add
     for field in form.fields.values():
        field.widget.attrs['class'] = 'form-control'

     return render(request, 'login.html', {'form': form})  

  #logout views 
# def logout_user(request):
#      logout(request)

#      return redirect('login')   



# def student_list(request):
#     data = students.objects.all()
#     return render(request, 'student_list.html', {'students': data})


# # Delete student data
# def delete_student(request, id):
#     student = students.objects.get(id=id)
#     student.delete()
#     return redirect('student_list')


# # Edit student data
# def edit_student(request, id):
#     student = students.objects.get(id=id)

#     if request.method == 'POST':
#         student.name = request.POST.get('name')
#         student.email = request.POST.get('email')
#         student.age = request.POST.get('age')
#         student.course = request.POST.get('course')
#         student.semester = request.POST.get('semester')

#         if request.FILES.get('photo'):
#             student.photo = request.FILES.get('photo')

#         student.save()

#         return redirect('student_list')

#     return render(request, 'edit_student.html', {'student': student})


# ### signin views ###
def signin(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(username=username)

        except CustomUser.DoesNotExist:
            return render(request, 'signin.html', {
                'error': 'Username not found'
            })

        if user.check_password(password):

            login(request, user)

            return redirect('homepage')

        return render(request, 'signin.html', {
            'error': 'Invalid password'
        })

    return render(request, 'signin.html')




# def signin(request):
#      if request.method =="POST":
#           username = request.POST.get('username')
#           password = request.POST.get('password')

#           user = CustomUser.objects.get(username = username)
#           if user.check_password(password):
#                login(request,user)
#                return redirect(homepage)
#      return render(request, 'signin.html')

  #logout views 
def logout_user(request):
     logout(request)

     return redirect('login')

### sigup view
# =========================
# SIGN UP
# =========================

def signup(request):

    context = {}

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_pass')

        if password != confirm_pass:

            context = {
                'error': 'Password and confirm password do not match.'
            }

            return render(request, 'signup.html', context)

        if CustomUser.objects.filter(username=username).exists():

            context = {
                'error': 'Username already exists.'
            }

            return render(request, 'signup.html', context)

        user = CustomUser(
            username=username
        )

        user.set_password(password)
        user.save()

        return redirect('signin')

    return render(request, 'signup.html', context)


# def signup(request):
#      context ={}
#      if request.method=="POST":
#           username = request.POST.get('username')
#           password = request.POST.get('password')
#           confirm_pass = request.POST.get('confirm_pass')

#           if password == confirm_pass:
#                user = CustomUser(
#                     username = username
#                    )
#                user.set_password(password)
#                user.save()
#           else:
#                context={
#                     'error':"password and confirm password Does not Matched."
#                }  
#           return render(request,'signup.html',context)
#      return render(request,'signup.html',context)  


def forget_pass(request):
    if request.method == "POST":
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        new_pass = request.POST.get('new_pass')
        conf_pass = request.POST.get('conf_pass')

        user = CustomUser.objects.get(email = email)

        if user.otp != int(otp):
            context = {
                'error' : "Your OTP is Invalid"
            }
            return render(request, 'forget_pass.html', context)

        if new_pass != conf_pass:
            context = {
                'error' : "Your Password don't Matched"
            }
            return render(request, 'forget_pass.html', context)

        user.set_password(new_pass)
        user.otp = None
        user.save()
        return redirect('signin')

    return render(request, 'forget_pass.html')


# =========================
# SEND OTP
# =========================
def send_otp(request):
    if request.method == "POST":
        email = request.POST.get('email')

        user = CustomUser.objects.get(email = email)

        otp = random.randint(111111,999999)
        user.otp = otp
        user.save()

        email_sub = f"""Your Forget Password OTP {otp}"""
        msg = f"""Your Forget Password OTP is {otp} \nPlease don't Share Your OTP with Anyone"""
        from_email = EMAIL_HOST_USER
        to_email = email

        send_mail(
            subject = email_sub,
            message = msg,
            from_email = from_email,
            recipient_list = [to_email]
        )
        return redirect('forget_pass')

    return render(request, 'send_otp.html')


# =========================
# UPDATE PASSWORD
# =========================



def update_pass(request):

    if request.method == "POST":

        email = request.POST.get('email')
        otp = request.POST.get('otp')
        new_pass = request.POST.get('password')
        confirm_pass = request.POST.get('confirm_pass')

        # Find user
        try:

            user = CustomUser.objects.get(email=email)

        except CustomUser.DoesNotExist:

            return render(request, 'update_pass.html', {
                'error': 'Email not found'
            })

        # Check OTP
        if not otp:

            return render(request, 'update_pass.html', {
                'error': 'Please enter OTP'
            })

        try:

            otp = int(otp)

        except ValueError:

            return render(request, 'update_pass.html', {
                'error': 'Invalid OTP'
            })

        if user.otp != otp:

            return render(request, 'update_pass.html', {
                'error': 'Your OTP is invalid'
            })

        # Check password
        
        if new_pass != confirm_pass:

            return render(request, 'update_pass.html', {
                'error': 'Your passwords do not match'
            })

        # Update password
        user.set_password(new_pass)

        # Remove OTP
        user.otp = None

        user.save()

        return redirect('signin')

    return render(request, 'update_pass.html')

               
# =========================
# CHANGE PASSWORD
# =========================
from .forms import ChangePasswordForm

def change_pass(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')

    else:
        form = ChangePasswordForm(request.user)    

    return render(request, 'change_pass.html', {'form' : form})