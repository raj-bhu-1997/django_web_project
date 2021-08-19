from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length= 20)
  text = models.CharField(max_length=200)
  image = models.ImageField(upload_to= 'images/%Y/%m/%d', blank = True, null = True)
  user = models.ForeignKey(User, on_delete = models.CASCADE)