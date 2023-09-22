from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE )
    city = models.ForeignKey('city',on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='profile/',null=True,blank=True,default='avatar.jpg')
    phone_number = models.PositiveIntegerField(null=True)

    def __str__(self):
        return str(self.user)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

class city(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
