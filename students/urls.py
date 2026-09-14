# from django.urls import path
# from django.urls import path
# from . import views



# urlpatterns = [
#     path('', views.student_list, name='student_list'),
#     path('delete/<int:id>/', views.delete_student, name='delete_student'),
#     path('edit/<int:id>/', views.edit_student, name='edit_student'),
# ]

# from django.urls import path
# from . import views 
# from django.conf.urls.static import static
# from django.conf import settings
# from students.views import register_user


from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    # Student
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),

    # Teacher
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/add/', views.add_teacher, name='add_teacher'),
    path('teachers/edit/<int:id>/', views.edit_teacher, name='edit_teacher'),
    path('teachers/delete/<int:id>/', views.delete_teacher, name='delete_teacher'),

    # Register / Login / Logout
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    path('forget_pass/', views.forget_pass, name='forget_pass'),

    # OTP
    path('send_otp/', views.send_otp, name='send_otp'),
    path('update_pass/', views.update_pass, name='update_pass'),
    

    # Change password
    path('change_pass/', views.change_pass, name='change_pass'),
    
    # path('search_teacher/', views.search_teacher, name='search_teacher'),
    
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )