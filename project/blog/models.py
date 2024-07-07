from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
