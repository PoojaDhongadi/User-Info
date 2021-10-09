from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from .models import User
from .forms import *

# Create your views here.

class LoginView(View):
    def get(self, request):
        fm = LoginForm()
        return render(request, 'core/login.html',{'form':fm})

    def post(self, request):
        fm = LoginForm(request, data=request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(request, username=username, password= password)
            if user is not None:
                login(request, user)
                return redirect('/show/')
            else:
                return render(request, 'core/login.html',{'form':fm})
        else:
            return render(request, 'core/login.html',{'form':fm})

class SignupView(View):
    def get(self, request):
        fm = AddUserForm()
        return render(request, 'core/signup.html',{'form':fm})
    
    def post(self, request):
        fm = AddUserForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/show/')
        else:
            return render(request, 'core/signup.html',{'form':fm})

class ShowDetails(View):
    def get(self, request):
        user_data = User.objects.all()
        return render(request, 'core/showdetails.html', {'userdata':user_data})


class DeleteUser(View):
    def post(self, request):
        data = request.POST
        id = data.get('id')
        userdata = User.objects.get(id=id)
        userdata.delete()
        return redirect('/show/')

class EditUser(View):
    def get(self, request, id):
        user = User.objects.get(id = id)
        fm = AddUserForm(instance=user)
        return render(request, 'core/editdetails.html',{'form':fm})  

    def post(self, request, id): 
        user = User.objects.get(id = id)
        fm = AddUserForm(request.POST, instance=user)
        if fm.is_valid():
            fm.save()
            return redirect('/show/')
        else:
            return redirect('/show/')
