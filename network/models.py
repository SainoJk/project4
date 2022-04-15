from datetime import datetime
from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class PostInfo(models.Model):
    spostuser=models.ForeignKey(User,on_delete=models.CASCADE,related_name="postuser")
    spostinfo=models.CharField(max_length=64)
    sposttime=models.DateTimeField(default=datetime.now,blank=True)
    spostlike=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.spostuser}:{self.spostinfo}"
    

class PostLike(models.Model):
     spostid=models.ForeignKey(PostInfo,on_delete=models.CASCADE,related_name="postid")
     slikeuser=models.ForeignKey(User,on_delete=models.CASCADE,related_name="likeuser")
     def __str__(self):
        return f"{self.slikeuser}-{self.spostid}"