from django.db import models
from django.urls import reverse

class BlogContent(models.Model):
    titleImg = models.ImageField(upload_to='previewIMG/')
    titleText = models.CharField(max_length=100)
    text = models.TextField()
    blog = models.ForeignKey('Blog', on_delete=models.PROTECT)


class Blog(models.Model):
    previewIMG = models.ImageField(upload_to='previewIMG/')
    previewTitle = models.CharField(max_length=100)
    previewText = models.CharField(max_length=500)
    slug = models.SlugField(null=True, db_index=True, unique=True)
    blogcollect = models.ForeignKey('BlogCollect', on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.previewTitle


class BlogCollect(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(null=True, db_index=True, unique=True)


    def get_absolute_url(self):
        return reverse('main:getBlogDetail', args=[self.slug])
    

    def __str__(self):
        return self.name