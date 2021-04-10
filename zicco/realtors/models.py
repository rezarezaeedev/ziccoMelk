from django.db import models

class Realtor(models.Model):
    fname       =   models.CharField(max_length=150,blank=True)
    lname       =   models.CharField(max_length=150,blank=True)
    phone       =   models.CharField(max_length=15,blank=True)
    address     =   models.TextField(blank=True)
    email       =   models.CharField(max_length=50,blank=True)
    instagram   =   models.CharField(max_length=25,blank=True)
    photo_main  =   models.ImageField(upload_to='profiles/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.fname} {self.lname}'
        
    
    
