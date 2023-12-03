from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User # handle users with django

# model.Models makes it a model by inheritence
class Task(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #if the user is deleted, the items are deleted as well
   title = models.CharField(max_length = 200)
   description = models.TextField(null=True, blank=True) #different than charfield
   complete = models.BooleanField(default=False)
   created = models.DateTimeField(auto_now_add=True) #take a snapshot
   priority = models.IntegerField(null=True, validators=[MinValueValidator(1),MaxValueValidator(10)])


   def __str__(self): #string representation of the model
      return self.title
   
   class Meta:
      ordering = ['complete', 'priority'] #this means the whenever completed, it goes to bottom (orderby)