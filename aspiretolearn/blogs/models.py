from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True) 
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category
    
class Tags(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=200)
    status = models.BooleanField(default=True) 
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.category.category
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.BooleanField(default=True) 
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.BooleanField(default=True) 
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.post.title