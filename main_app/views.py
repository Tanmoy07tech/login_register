from django.core.checks import messages
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from main_app.models import Student
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


# Create your views here.
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def home(request):
   
    return render(request,'home.html')


def login(request):
    if request.method=='POST':
        all_students=Student.objects.all()
        college_id=request.POST.get('collegeid')
        
        raw_pass=request.POST.get('password')
       
        
        verify=False
        for member in all_students:
            password_log=check_password(raw_pass,encoded=member.password)
            
            if college_id==member.college_id and password_log:    
                print('succesfully logged')
                verify=True
                return HttpResponse('Loggin Successfull')
                
            elif college_id==member.college_id and password_log!=member.password:    
                messages.error(request,'Invalid Password')

                return render(request,'login.html')
        if verify==False:   
            messages.error(request,'No registered College Id found.Please register first')

            return render(request,'login.html')   
    return render(request,'login.html')
            
   
    

def register(request):
    if request.method=='POST':
        all_students=Student.objects.all()
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        collegeid=request.POST.get('collegeid')
        password=make_password(request.POST.get('password'))
        verify=False
        
        if all_students.exists()==False:
            print('In if all students')
            s1=Student(first_name=firstname,last_name=lastname,college_id=collegeid,email=email,password=password)
            s1.save()  
            print('Created a account')
            messages.success(request,'Succesfully created an account.Please Login')
                
            return render(request,'login.html')
            
        else:
            for member in all_students:
                if collegeid == member.college_id:
                    
                    messages.error(request,'Student with this College id already exists.Please Login using the same')
                    return render(request,'register.html')

                elif email == member.email:
                    messages.error(request,'Account is already registered with this email.Use some other mail')
                    return render(request,'register.html')
                else:
                    verify=True
            if verify==True:
                s1=Student(first_name=firstname,last_name=lastname,college_id=collegeid,email=email,password=password)
                s1.save()  
                print('Created a account')
                messages.success(request,'Succesfully created an account.Please Login')
                
                return render(request,'login.html')
            
    
    return render(request,'register.html')



