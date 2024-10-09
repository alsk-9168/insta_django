from django.db import models

# Create your models here.
class Insta_data(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.username} - {self.password}'