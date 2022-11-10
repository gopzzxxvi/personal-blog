from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    ID = models.CharField(max_length=36, primary_key=True)
    Title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    Date_created = models.DateTimeField(auto_now_add=True)
    Content = models.TextField()

    views = models.IntegerField(default=0)
    Likes = models.IntegerField(default=0)

    def __str__(self):
        return self.Title + " By " + self.user.get_username()

class Comment(models.Model):
    Blog_ID = models.ForeignKey(Post, on_delete=models.CASCADE)

    User_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Date_created = models.DateTimeField(auto_now_add=True)
    Content = models.TextField()