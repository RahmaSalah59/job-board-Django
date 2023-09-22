from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
JOB_TYPE = (
    ('Full_Time','Full_Time'),
    ('Part_Time','Part_Time'),
)

GENDER  = (
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
)

def image_save(instance,filename):
    image_name,extinsion = filename.split('.')
    return "jobs/%s.%s"%(instance.id,extinsion)


class category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    
class job(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # locatoin ...  
    type = models.CharField(max_length=100,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    puplished_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category_name = models.ForeignKey(category,on_delete=models.CASCADE,null=True,blank=True) 
    experience = models.IntegerField(default=1)
    gender = models.CharField(max_length=100,choices=GENDER) 
    image = models.ImageField(upload_to=image_save)
    slug = models.SlugField(blank=True,null=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)  
        super(job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Apply(models.Model):
    apply_job = models.ForeignKey(job,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    website = models.URLField()
    cv = models.FileField(upload_to="apply/")
    coverletter = models.TextField(max_length=1000)
    apply_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name