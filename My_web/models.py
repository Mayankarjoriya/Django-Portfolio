from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    desc = models.TextField()
    pub_date = models.DateField()


