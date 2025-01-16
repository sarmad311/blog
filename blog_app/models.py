from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')

    def __str__(self):
        return self.title