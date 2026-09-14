from django import forms
from .models import student, teacher, Profile,  CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth.forms import CustomUser
from django.contrib.auth.forms import PasswordChangeForm


class studentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'course', 'semester', 'age']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'course': forms.TextInput(attrs={'class': 'form-control'}),
            'semester': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }

#teacher forms

class teacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['name','email','department','designation','age']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class UserRegistrationForm(UserCreationForm):
    
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={ 
               'class' : 'form-control',
               'placeholder' : 'Inputusername'
               
               }
        ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Input email'
        }
        ))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input password1'
            }
        ))
    password2 = forms.CharField(widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Input password2'
                }
            ))
    
    role = forms.ChoiceField(choices=[('student', 'Student'),('teacher', 'Teacher')], widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']
    widget = {
        'username': forms.TextInput(attrs={'class' : 'form-control'}),
        'email':forms.EmailInput(attrs={'class' : 'forms-control'}),
    }
    
class userloginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder' : 'Input username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input password'
        }
    ))
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
        
class ChangePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Old Password'
        }
    ))
    new_password1 = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input New Password'
        }
    ))
    new_password2 = forms.CharField(label="",widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Input Confirm Password'
        }
    ))
    
    


def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()

            Profile.objects.create(
                user=user,
                role=self.cleaned_data['role']
            )

        return user
