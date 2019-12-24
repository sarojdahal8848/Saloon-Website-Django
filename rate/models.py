from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250,null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=250,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    gender = models.CharField(max_length=8,null=True)
    time = models.CharField(max_length=250,null=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)


    def __str__(self):
        return self.name
