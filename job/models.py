from django.db import models
from django.utils import timezone


# Create your models here.


Job_Time_choices = (
    ('Full Time','Full Time'),
    ('Part Time', 'Part Time'),
)
class Job(models.Model):
    title            = models.CharField(max_length = 100) 
    # location
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    job_type         = models.CharField(max_length=15 , choices  = Job_Time_choices)
    discription      = models.TextField(max_length=1000 )
    publish          = models.DateTimeField(default  = timezone.now)
    updated          = models.DateTimeField(auto_now_add=True)
    vacancy          = models.IntegerField(default = 1)
    salary           = models.IntegerField(default = 0)
    
    experience       = models.IntegerField(default = 1 )
    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title


class Category(models.Model):
    name   = models.CharField(max_length=50)

    def __str__(self):
        return self.name



