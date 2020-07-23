from django.shortcuts import get_object_or_404, redirect, render
from .models import Job , Category
from .forms import JobApplyForm , JobForm
from django.core.paginator import Paginator


# Create your views here.


def job_list(request):
    job_list =Job.objects.all()

    # pagination 
    paginator     = Paginator(job_list , 3)
    page_number   = request.GET.get('page')
    page_obj      = paginator.get_page(page_number)
    context = {
        'jobs':page_obj , 
    }
    return render(request, 'job/jobs.html', context)
    
 

def job_detail(request,slug):
    job  = get_object_or_404(Job , slug = slug)
    if request.method == 'POST':
        form = JobApplyForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.job_apply = job
            new_form.save()
          
            
            
    else : 
        form = JobApplyForm()
    context = {
        'job':job , 
        'form':form,
    }
    return render(request, 'job/job_details.html', context)
    

# add job 

def add_job(request):
    if request.method =="POST":
        form = JobForm(request.POST , request.FILES) 
        if form.is_valid():
            new_form =form.save(commit=False)
            new_form.job_owner = request.user
            new_form.save()
            return redirect('/jobs')
            
    else:
        form = JobForm()
    context = {
        'form':form,
    }
    return render(request, 'job/add_job.html', context)
    