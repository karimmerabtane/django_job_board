from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


Job_Time_choices = (
    ('Full Time','Full Time'),
    ('Part Time', 'Part Time'),
)

def image_upload(instance , filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id , extension)
class Job(models.Model):
    title            = models.CharField(max_length = 100) 
    slug             = models.SlugField(null= True , blank = True)
    # location
    category         = models.ForeignKey('Category', on_delete=models.CASCADE)
    job_type         = models.CharField(max_length=15 , choices  = Job_Time_choices)
    discription      = models.TextField(max_length=1000 )
    publish          = models.DateTimeField(default  = timezone.now)
    updated          = models.DateTimeField(auto_now_add=True)
    vacancy          = models.IntegerField(default = 1)
    salary           = models.IntegerField(default = 0)
    experience       = models.IntegerField(default = 1 )
    image            = models.ImageField( upload_to=image_upload)
    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("jobs:job_detail", args=[self.slug])


    def save(self , *args, **kwargs):
        self.slug   = slugify(self.title)
        super(Job ,self).save(*args, **kwargs)


class Category(models.Model):
    name   = models.CharField(max_length=50)

    def __str__(self):
        return self.name



# models job apply

class JobApply(models.Model):
    job_apply         = models.ForeignKey( Job , on_delete=models.CASCADE , related_name='jobapply')
    name        = models.CharField(max_length = 50)
    email       = models.EmailField()
    website     = models.URLField()
    cv          = models.FileField( upload_to='job_apply_cv/')
    discription = models.TextField()
    apply_at    = models.DateTimeField( auto_now=True)  

    def __str__(self):
        return self.name

   
