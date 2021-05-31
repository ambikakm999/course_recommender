from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
from .forms import ProfileUpdateForm, CreateUserForm
from django.contrib import messages
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory

# Create your views here.
#@login_required
def home(request):
    #context={'prim_key':pk}
    return render(request,'home.html')

#@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #group=Group.objects.get(name='student')
            #user.groups
            #Student.objects.create(username=user,name=user.username)

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')#pk=request.user.pk)

    context = {'form': form}
    return render(request, 'signup.html', context)

#@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')#pk=request.user.pk)
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
        logout(request)
        return redirect('login')

def editprofile(request):  #pk):
    #if request.method == 'POST':
        #form = ProfileUpdateForm(data=request.POST, instance=request.user)
        #update=form.save()
        #update.user=request.user
        #update.save()

    #else:
        #form = ProfileUpdateForm(instance=request.user)

    #context = {'form': form}

    #editinfo = Student.objects.get(id=pk)
    #form = ProfileUpdateForm(instance=editinfo)

    #if(request.method=='POST'):
        #form=ProfileUpdateForm(request.POST,instance=editinfo)
        #if form.is_valid():
            #form.save()
            #redirect('home')

    #context={'form':form}
    profile = request.user.student
    form = ProfileUpdateForm(instance=profile)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'editprofile.html', context)

def ratecourse(request):
    courses=Course.objects.all()

    form=RateForm()
    if request.method == 'POST':
        form = RateForm(request.POST)

        if form.is_valid():
            form.save()

    context={'courses':courses,'form':form}

    return render(request,'ratecourse.html',context)
