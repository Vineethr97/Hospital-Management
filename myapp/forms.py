from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Doctor,Appointment,Department



class SignUpForm(UserCreationForm):
  

    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields={"patientName","email","phone","place","date","doctorName","time"}

        widgets={
            "patientName":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone":forms.TextInput(attrs={"class":"form-control"}),
            "place":forms.TextInput(attrs={"class":"form-control"}),
            "date":forms.TextInput(attrs={"class":"form-control"}),



             "doctorName":forms.TextInput(attrs={"class":"form-control"}),


        }
   

class DoctorDepartmentForm(forms.ModelForm):
    class Meta:
        model=Doctor
        
        fields=["name","department","qualification","profile_pic"]
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "qualification":forms.TextInput(attrs={"class":"form-control"}),
            "profile_pic":forms.FileInput(attrs={"class":"form-control"})
        }
        


        
class DoctorDepartmentEditForm(forms.ModelForm):
    class Meta:  
        model=Doctor 
        fields=["name","department","qualification","profile_pic"] 
        widgets={   
            "name":forms.TextInput(attrs={"class":"form-control"}), 
            
            "qualification":forms.TextInput(attrs={"class":"form-control"}), 
            "profile_pic":forms.FileInput(attrs={"class":"form-control"})   
        }


class DepartmentForm(forms.ModelForm):
    class Meta:  
        model=Department
        fields=["department"] 

        widgets={   
            "department":forms.TextInput(attrs={"class":"form-control"}), 
             
            }
        

class DepartmentEditForm(forms.ModelForm):
    class Meta:  
        model=Department
        fields=["department"] 

        widgets={   
            "department":forms.TextInput(attrs={"class":"form-control"}), 
            
             
            }