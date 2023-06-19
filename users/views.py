from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime

from .forms import *
from django.template.context_processors import csrf

# Create your views here.
def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm(request.POST)
    return render(request,'users/register.html',{'form':form})  


@login_required
def profile(request):
    today = datetime.datetime.now()
    current_user = request.user
    if request.method == 'POST':
        profile_form = ProfileUpdateForm (request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('dashboard')
    else:
        profile_form = ProfileUpdateForm (instance=request.user.profile)

    context = {
        'current_user': current_user,
        'profile_form': profile_form,
        'today': today
    }
    return render(request, 'users/profile.html', context)

