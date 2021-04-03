from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import datetime

class Blog( models.Model):
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    title= models.CharField(max_length=150)
    dsc= models.TextField()
    date= models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title
    