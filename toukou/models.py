from django.db import models

class PostModel(models.Model):
    title = models.CharField(max_length=50)
    memo = models.TextField()

    def __str__(self):
        return self.title