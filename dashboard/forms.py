from django import forms
from .models import UploadPDF, Department, Employee

# Create Here
class UploadPDFForm(forms.ModelForm):
    employee = forms.ModelChoiceField(queryset=Employee.objects.all(), widget=forms.Select(attrs={
                                                                                                    'class':'my-select',
                                                                                                    'placeholder': 'Select an employee...'
                                                                                                }))
    
    class Meta:
        model = UploadPDF
        fields = ['employee','subject', 'pdf_file']


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department
        fields = ['department_name']


class EmployeeForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), widget=forms.Select(attrs={
                                                                                                    'class':'my-select',
                                                                                                    'placeholder': 'Select a department...'
                                                                                                }))

    class Meta:
        model = Employee
        fields = ['full_name', 'email', 'phone_number', 'national_id', 'image', 'department', 'job_title']