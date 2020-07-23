from django.urls import include, path
from . import views


app_name ='job'

urlpatterns = [
    path ('' , views.job_list , name = 'job_list'), 
    path('add_job/', views.add_job, name='add_job'),
    path('<slug:slug>/', views.job_detail , name = 'job_detail'),

]
