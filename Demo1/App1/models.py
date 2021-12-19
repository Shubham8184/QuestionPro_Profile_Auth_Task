from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


#---------CustomUser Model -------------------------
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)
    mobile_no=models.BigIntegerField(unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True,
                                  null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=True,
                                 null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_no']
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"


#------Profile Models--------------------
class Profile(models.Model):
    gender_list=[('male','male'),('female','female'),('other','other')]
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    gender=models.CharField(choices=gender_list,max_length=50)
    profile_dp=models.ImageField(upload_to='profile/',blank=True,null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

