from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogItem(models.Model):
    # point to a specific user, if user is deleted, delete in the database
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    post = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    # return string to admin panel, to see which user has added which item
    def __str__(self):
        return f"{self.pk}, {self.title}, by {self.user}"