from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    return render(request, 'dashboard/landing.html')


@login_required
def dashboard(request):
    current_user = request.user
   
    context = {
        
        'current_user':current_user
    }
    
    return render(request, 'dashboard/dashboard.html', context)