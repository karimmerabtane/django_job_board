from django.contrib import admin
from .models import Job ,Category , JobApply
# Register your models here.

# add models job to admin 
admin.site.register(Job)
# add category
admin.site.register(Category)

# add job apply models 

admin.site.register(JobApply) 