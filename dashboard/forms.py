from django import forms
from .models import UploadPDF

# Create Here
class UploadPDFForm(forms.ModelForm):
    
    class Meta:
        model = UploadPDF
        fields = ['subject', 'pdf_file']