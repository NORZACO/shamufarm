from django.db import models
# Create your models here.
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


# user category
class Category(models.Model):
    name=models.CharField("Category Name",max_length=256,unique=True,)
    images = models.ImageField(default="empty-images.jpg")
    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    images = models.ImageField(default="empty-images.jpg")
    #slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # category
    category  = models.ManyToManyField(Category, related_name ='post' )
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
