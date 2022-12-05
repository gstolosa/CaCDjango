from django.db import models

class Contact(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=40)
    message = models.TextField(max_length=400)

    def __str__(self):
        return self.lname
