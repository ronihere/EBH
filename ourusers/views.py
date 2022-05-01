from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from . forms import userregistrationform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    print(request.method)
    if request.method == 'POST':
        form = userregistrationform(request.POST)



        if form.is_valid():

            form.save()


            username= form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username}')
            return redirect('/login')

        else:


            return render(request,'register.html',{'form':form})

    else:
        form = userregistrationform()

        return render(request,'register.html',{'form':form})

def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request,f'password or username is incorrect')
    return render(request,'login.html')


@login_required(login_url='login')
def home(request):
    return redirect('book/home')

@login_required(login_url='login')
def logoutpage(request):
    logout(request)
    return redirect('login')