from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.
class UploadPDF(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pdf')
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='employee_pdf', blank=False, null=False, default=1)
    subject = models.CharField(max_length=50, blank=True, null=True)
    pdf_file = models.FileField(upload_to='media/files/')
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-upload_date']


class Employee(models.Model):
    full_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone_number = models.CharField(max_length=25, blank=False, null=False)
    national_id = models.CharField(max_length=25, blank=False, null=False)
    image = CloudinaryField ('image')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, related_name='employee_department', blank=False, null=False, default=1)
    job_title = models.CharField(max_length=100, blank=True, null=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.full_name)


class Department(models.Model):
    department_name = models.CharField(max_length=100, blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.department_name)