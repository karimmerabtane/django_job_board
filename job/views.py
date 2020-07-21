from django.shortcuts import get_object_or_404, render
from .models import Job , Category

# Create your views here.


def job_list(request):
    job_list =Job.objects.all()
    context = {
        'jobs':job_list , 
    }
    return render(request, 'job/jobs.html', context)
    
 

def job_detail(request,id):
    job  = get_object_or_404(Job , id = id)
    context = {
        'job':job , 
    }
    return render(request, 'job/job_details.html', context)
    
