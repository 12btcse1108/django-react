from django.db import models

# Create your models here.

class Tutorial(models.Model):
    title = models.CharField(max_length = 500)
    body = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)

    def __str__(self):
        return self.title
