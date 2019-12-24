from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=250,null=True)
    author = models.CharField(max_length=250,null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='images/')
    published = models.BooleanField(default=True)
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)



    def __str__(self):
        return self.title

    class meta:
        ordering = ['-created_at']