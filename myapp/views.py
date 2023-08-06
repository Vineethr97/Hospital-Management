from django.shortcuts import render,redirect
from django.views.generic import CreateView,FormView,TemplateView,ListView,UpdateView,DetailView,View
from django.contrib.auth.models import User
from myapp.forms import SignUpForm,LoginForm,AppointmentForm,DoctorDepartmentForm,DoctorDepartmentEditForm,DepartmentForm,DepartmentEditForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from myapp.models import Doctor,Appointment,Department
from django.utils.decorators import method_decorator

def sign_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("signin")
        return fn(request,*args,**kwargs)
    return wrapper



class signUpView(CreateView):
    model=User
    template_name="register.html"
    form_class=SignUpForm
    success_url=reverse_lazy("signin")
    
    def form_valid(self, form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"faild to create account")
        return super().form_invalid(form)
    


class SignInView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login successfully")
                return redirect("index")
            messages.error(request,"invalid creadential")
            return render(request,self.template_name,{"form":form})
        
@method_decorator(sign_required,name="dispatch")
class HomeView(TemplateView):
    template_name="home.html"

@method_decorator(sign_required,name="dispatch")
class AppointmentView(CreateView):
    model=User
    template_name="appointment.html"
    form_class=AppointmentForm
    success_url=reverse_lazy("appointmentlist")
    def form_valid(self,form):
        messages.success(self.request,"successful")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request,"failed to make appointment")
        return super().form_invalid(form)
@method_decorator(sign_required,name="dispatch")   
class AppointmentListView(ListView):
    model=Appointment
    template_name="appointmentlist.html"
    context_object_name="appointments"




@method_decorator(sign_required,name="dispatch")
class IndexView(TemplateView):
    template_name="index.html"


def sign_out_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logout")
    return redirect("home")


@method_decorator(sign_required,name="dispatch")
def doctor_delete_view(request,*args,**kwargs):
    id=kwargs.get("pk")
    Doctor.objects.get(id=id).delete()
    messages.success(request,"doctor removed")
    return redirect("doctorlist")
 


@method_decorator(sign_required,name="dispatch")
class DoctorDepartmentView(CreateView):
    model=Doctor
    template_name="doctorcreate.html"
    form_class=DoctorDepartmentForm
    success_url=reverse_lazy("doctorlist")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"doctor has been created")
        return super().form_valid(form)



@method_decorator(sign_required,name="dispatch")
class DoctorDepartmentListView(ListView):
    model=Doctor
    template_name="doctorlist.html"
    context_object_name="doctors"


@method_decorator(sign_required,name="dispatch")
class DoctorDepartmentEditView(UpdateView):
    model=Doctor
    form_class=DoctorDepartmentEditForm
    template_name="doctoredit.html"
    success_url=reverse_lazy("doctorlist")

    def form_valid(self, form):
        messages.success(self.request,"changed")
        return super().form_valid(form)
    
@method_decorator(sign_required,name="dispatch")
class DoctorDetailView(DetailView):
    model=Doctor
    template_name="doctordetail.html"
    context_object_name="doctor"



@method_decorator(sign_required,name="dispatch")
class DepartmentCreateView(CreateView):
    model=Department
    template_name="department.html"
    form_class=DepartmentForm

    success_url=reverse_lazy("departmentlist")
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"department has been created")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request,"failed to create department")
        return super().form_invalid(form)
    

@method_decorator(sign_required,name="dispatch")
class DepartmentListView(ListView):
    model=Department
    template_name="departmentlist.html"
    context_object_name="departments"

@method_decorator(sign_required,name="dispatch")
class DepartmentDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Department.objects.get(id=id).delete()
        return redirect("departmentlist")
    
@method_decorator(sign_required,name="dispatch")
class DepartmentEditView(UpdateView):
    model=Department
    form_class=DepartmentEditForm
    template_name="departmentedit.html"
    success_url=reverse_lazy("departmentlist")

    def form_valid(self, form):
        messages.success(self.request,"changed")
        return super().form_valid(form)