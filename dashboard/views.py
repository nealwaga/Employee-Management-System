from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime

from .forms import UploadPDFForm
from .models import UploadPDF

# Create your views here.
def landing(request):
    return render(request, 'dashboard/landing.html')


@login_required
def dashboard(request):
    today = timezone.now()
    current_user = request.user
    pdfs = UploadPDF.objects.filter(user=current_user).all()

    # Form validation
    if request.method == 'POST':   
        form = UploadPDFForm(request.POST, request.FILES)        
        if form.is_valid:   
            pdf = form.save(commit=False)
            pdf.user = current_user
            pdf.save()   
            return redirect('dashboard')   
    else:    
        form = UploadPDFForm()
   
    context = {
        'today': today,
        'current_user':current_user,
        'form':form,
        'pdfs':pdfs,
    }
    return render(request, 'dashboard/dashboard.html', context)