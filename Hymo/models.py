from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Doctors(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    fathers_name = models.EmailField(max_length=200)


    def __str__(self):
        return str(self.name
        
        )

    
    


    # class Meta:
    #     model = User
    #     fields = ("first_name", "last_name", "email", "password")


    

