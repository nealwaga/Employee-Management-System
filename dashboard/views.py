from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import FileResponse
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

@login_required
def view_pdf(request, pdf_id):
    pdf = get_object_or_404(UploadPDF, id=pdf_id)
    return FileResponse(pdf.pdf_file)