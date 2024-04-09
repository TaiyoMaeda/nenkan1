from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

class Blog(models.Model):
    blog_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

