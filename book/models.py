from django.db import models



class Book(models.Model):
    fname = models.CharField(max_length=250,null=True)
    lname = models.CharField(max_length=250,null=True)
    phone = models.CharField(max_length=15,null=True)
    address = models.TextField(null=True)
    datetime = models.CharField(max_length=250,null=True)
    service = models.CharField(max_length=250,null=True)
    created_on = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.fname + self.lname + self.datetime

