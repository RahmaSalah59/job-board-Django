from django.db import models

# Create your models here.
JOB_TYPE = (
    ('FULL_TIME','FULL_TIME'),
    ('PART_TIME','PART_TIME'),
)

GENDER  = (
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
)

class job(models.Model):
    title = models.CharField(max_length=100)
    # locatoin ...  
    type = models.CharField(max_length=100,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    puplished_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    #category ... 
    experience = models.IntegerField(default=1)
    gender = models.CharField(max_length=100,choices=GENDER) 

    def __str__(self):
        return self.title
