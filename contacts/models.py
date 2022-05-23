from tkinter import Misc
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    misc = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length= 400)
    
    def __str__(self):
        return str(self.author) + '|' + str(self.id)