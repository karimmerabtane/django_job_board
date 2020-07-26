from django.urls import include, path
from . import views
from . import api


app_name ='job'

urlpatterns = [
    path ('' , views.job_list , name = 'job_list'), 
    path('add_job/', views.add_job, name='add_job'),
    path('<slug:slug>/', views.job_detail , name = 'job_detail'),
    # api url 

    path('api/list', api.job_list_api, name='joblist_api'),
    path('api/<int:id>', api.job_detaill_api, name='job_detaill_api'),
    # class based views 
    path('api/v2/<int:id>', api.JobDetail.as_view(), name='JobDetail'),
    path('api/list/v2/', api.JobList.as_view(), name='listclass'),

]
