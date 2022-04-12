from datetime import datetime
from email.policy import default
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class PostInfo(models.Model):
    spostuser=models.ForeignKey(User,on_delete=models.CASCADE,related_name="postuser")
    spostinfo=models.CharField(max_length=64)
    spostlike=models.IntegerField(default=0)
    sposttime=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return f"{self.spostuser}:{self.spostinfo}"
    

""" class PostComment(models.Model):
     s_user_comment=models.ForeignKey(User,on_delete=models.CASCADE,related_name="postuser_comment")
     s_postid_comemnt=models.ForeignKey('PostInfo',on_delete=models.CASCADE,related_name="postid_comment")
     s_comment=models.CharField(max_length=64)
     def __str__(self):
        return f"{self.spostuser}-{self.spostid}:{self.scomment}" """