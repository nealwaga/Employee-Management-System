from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UploadPDF(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pdf')
    subject = models.CharField(max_length=50, blank=True, null=True)
    pdf_file = models.FileField(upload_to='media/files/')
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-upload_date']