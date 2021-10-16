from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Create your models here.
class Profile(models.Model):
    profile_image = CloudinaryField('image', null=True,default = 'default.jpg')
    bio = models.TextField(default="")
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
        
class Post(models.Model):
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    image = CloudinaryField('image', null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default = timezone.now) 
    likes = models.IntegerField(default=0)
    location = models.CharField(max_length=80, null=True)


    @classmethod
    def search_by_location(cls,search_term):
        photos = cls.objects.filter(author__icontains = search_term)   
        # We filter the model data using the __icontains query filter
        return photos    
   

    def __str__(self):
        return self.caption        
        
class Likes(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='user_like')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_likes')

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete = models.CASCADE,related_name='comments')
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return '%s - %s' % (self.post.caption, self.name)
            