from .models import Job 
from django.shortcuts import get_object_or_404
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from rest_framework import generics



@api_view(['GET'])
def job_list_api(request):
    all_job = Job.objects.all()
    data    = JobSerializer(all_job,many = True).data
    return Response({'data':data})


# return job detail 

@api_view(['GET'])
def job_detaill_api(request,id):
    job_detaill = Job.objects.get(id = id)
    data = JobSerializer(job_detaill).data
    return Response({'data': data})



# class add delet detail 

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset         = Job.objects.all()
    lookup_field     = 'id'


class JobList(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    
