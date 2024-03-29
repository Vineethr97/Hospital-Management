

from django.db import models
from django.contrib.auth.models import User



departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class Doctor(models.Model):
    name=models.CharField(max_length=100,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    mobile = models.CharField(max_length=20,null=True)
    qualification=models.CharField(max_length=120)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    
    def _str_(self):
        return self.user.username
    




    
timeslot=[('morning','morning'),('afternoon','afternoon'),('evening','evening')]
   

class Appointment(models.Model):
    patientName=models.CharField(max_length=40,null=True)
    email=models.EmailField(null=True)
    phone=models.CharField(max_length=20,null=True)
    place=models.CharField(max_length=100,null=True)
    date=models.CharField(max_length=100,null=True)
    time=models.CharField(max_length=100,choices=timeslot,default='morning')
    department=models.CharField(max_length=100,choices=departments,default='cardiologist')
    doctorName=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.patientName
   

class Department(models.Model):
    department=models.CharField(max_length=250)
    
    def _str_(self):
        return self.department



