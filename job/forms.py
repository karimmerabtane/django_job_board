from django import forms
from .models import JobApply , Job


class JobApplyForm(forms.ModelForm):
    
    class Meta:
        model = JobApply
        fields = ("name", "email", "website", "cv", "discription")

class JobForm(forms.ModelForm):
    
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['slug','job_owner']
        
