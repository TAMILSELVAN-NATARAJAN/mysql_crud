from django.shortcuts import render,redirect
from base.form import EmployeeForm
from base.models import Employee
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate ,login,logout

# Create your views here.
def signup(request):
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form =UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username')
            password =form.cleaned_data.get('password1')
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')
        else:
            return render(request,'base/signup.html',{'form':form})
        
    else:
         form=UserCreationForm()
         return render(request,'base/signup.html',{'form':form})
        
def signout(request):
       logout(request)
       return redirect('/')

def signin(request):
    form=AuthenticationForm(request)

    if request.user.is_authenticated:
        return render(request,'base/home.html')
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/profile')
        else:
            msg="Login Error"
            form=AuthenticationForm(request.POST)
            return render(request,'base/login.html',{'form':form,'msg':msg})
    else:
        form =AuthenticationForm()
        return render(request,'base/login.html',{'form':form})

def profile(request):
    return render(request,'base/profile.html')
    
   
   


def home(request):
    emp = Employee.objects.all()
    context ={'emp':emp}
    return render(request,'base/home.html',context)

def adduser(request):
    form=EmployeeForm()
    
    if request.method == 'POST':
        form =EmployeeForm(request.POST)
        try:
            form.save()
            return redirect('/')
     
        except:
            pass 
    else:
        form=EmployeeForm() 
    context={'form':form}
    return render(request,'base/adduser.html',context)

def edit(request,id):
    employee =Employee.objects.get(id=id)
    context={'employee':employee}
    return render(request,'base/edit.html',context)

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)

    if form.is_valid():
         form.save()
         return redirect('/')
       

    context={'employee':employee}
    return render(request,'base/edit.html',context)

def delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/')

