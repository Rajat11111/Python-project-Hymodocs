from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Doctors





def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['psw']
        try:
            email_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            email_obj = None
        if email_obj is not None:
            user = authenticate(username=email_obj.first_name+email_obj.last_name , password=password)
            if user is None:
                return render(request, 'Hymo/index.html')
            return redirect("/details/")
        else:
            return render(request, 'Hymo/signup.html')
    return render(request, 'Hymo/index.html')
   

        



               
           


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['Firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['psw']
        email_obj = User.objects.filter(email=email)
        
        if len(email_obj) == 0:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, password=password, username=first_name+last_name)
            messages.success(request,'User Created Successfully')
            return redirect("/")
        else:
            messages.error(request,"Email Is Already Exist")
            return redirect("/")

                
    return render(request, 'Hymo/signup.html')
            
       
        

    

def details(request):
    doctor = Doctors.objects.all()
    context = {
        "doctor" : doctor
        }

    return render(request, "hymo/details.html", context)
  



def adddoctor(request):
    if request.method == 'POST':
        name = request.POST['name']
        degree = request.POST['degree']
        fathers_name = request.POST['fathers_name']
        doctor = Doctors.objects.create(name=name, degree=degree, fathers_name=fathers_name)

        messages.success(request, "data has been saved")     
        return render(request, 'Hymo/add.html')



    return render(request, 'Hymo/add.html')


def editdoctor(request, id):
    if request.method == "POST":
        name = request.POST['name']
        degree = request.POST['degree']
        fathers_name = request.POST['fathers_name']
        doctor = Doctors.objects.filter(id=id).update(name=name, degree=degree, fathers_name=fathers_name)
        messages.success(request, "data has been saved")     
        return redirect("/details/")
    
    doctor = Doctors.objects.get(id = id)
    context = {
        "doctor" : doctor
    }
    print('----------------------->')
    return render(request, "hymo/edit.html", context)




def delete(request, id):
    try:
        doctor = Doctors.objects.get(id=id)
        doctor.delete()
        return redirect('/details/')
    except Doctors.DoesNotExist:
        return redirect('/details/')







            
        
        
        
    

    





