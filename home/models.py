from django.db import models




class Saying(models.Model):
    fullname = models.CharField(max_length=250,null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.TextField(null=True)

    def __str__(self):
        return self.fullname

class Contact(models.Model):
    fullname = models.CharField(max_length=250,null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
    subject = models.CharField(max_length=250,null=True)


    def __str__(self):
        return self.fullname


class Team(models.Model):
    fname = models.CharField(max_length=250,null=True)
    lname = models.CharField(max_length=250,null=True)
    phone = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    image = models.ImageField(upload_to='images/')
    gender = models.CharField(max_length=8,null=True)
    position = models.CharField(max_length=250,null=True)
    age = models.CharField(max_length=5,null=True)
    experience = models.CharField(max_length=25,null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.fname + self.lname
    

class Gallery(models.Model):
    category = models.CharField(max_length=250,null=True)
    image = models.ImageField(upload_to='images/')
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.category


class Review(models.Model):
    fullname = models.CharField(max_length=250,null=True)
    designation = models.CharField(max_length=250,null=True)
    message = models.TextField(null=True)
    RATING_RANGE = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    rating = models.IntegerField(choices=RATING_RANGE)
    image = models.ImageField(upload_to='images/', null=True)
    created_on = models.DateField(auto_now=True)


    def __str__(self):
        return self.fullname

    class meta:
        ordering = ['-created_at']


