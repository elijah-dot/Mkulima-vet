# Create your models here.
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


OUR_PETS = (
    ("Cat","cat"),
    ("Dog","dog"),
    ("Parrot","parrot"),
    ("Rabbit","Rabbit"),
    ("Guinea pig","guinea pig"),
)



class Vet(models.Model):
    name = models.CharField(max_length=120)
    speciality = models.CharField(max_length=120)
    image = models.ImageField(upload_to="doctors/")



    def __str__(self):
        return self.name
    


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "profile",default=None,null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    image = models.ImageField(upload_to='images')
    bio = models.CharField(max_length=100000)
    phone = models.IntegerField()
    
    
    
class Testimonial(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(upload_to="feedback/")

class Pet(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255, blank=True, choices=OUR_PETS)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
       
    
    
# class Pet_owner(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     name_pet = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='images/')
    

    
class Contact(models.Model):
    email= models.EmailField(max_length=255)
    subject= models.CharField(max_length=255)
    message= models.TextField(max_length=255)
    
    def __str__(self):
        return self.email 
    
class Appointment(models.Model):

    choices_time = (
        ('0800hrs','0800-0900'),
        ('0930hrs', '0930-1130'),
        ('noon','1200-0130'),
        ('1400hrs', '0200-0300'),
        ('1530hrs', '0330-0430'),
    )


    choices_services = (
        ('Grooming','Grooming'),
        ('Vaccination','Vaccination'),
        ('Diet and Nutrition','Diet and Nutrition'),
        ('Weight Mnagement','Weight Management'),
        ('Behavior','Behavior'),
        ('Oral and Dental Exam','Oral and Dental Exam'),
        (' Photoshoot',' Photoshoot'),

    )





    pet = models.ForeignKey(Pet, on_delete=models.SET_NULL, blank=True, null=True) ###ADDING PETS
    vet = models.ForeignKey(Vet, related_name='the_vet',on_delete=models.SET_NULL,blank=True,null=True) ###ADDING
    date = models.DateTimeField() # Date input type....
    service = models.CharField(choices=choices_services, max_length=35)
    time_booked = models.CharField(choices=choices_time, max_length=10)
    when_the_booking_was_done = models.DateTimeField(auto_now_add=True)
    pet_owner = models.ForeignKey(User,on_delete=models.CASCADE)

   
