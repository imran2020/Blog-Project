from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class author(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture=models.FileField()
    details=models.TextField()

    def __str__(self):
        return self.name.username

class category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class article(models.Model):
    article_author=models.ForeignKey(author,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    image=models.FileField()
    body=RichTextUploadingField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    posted_on=models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True,auto_now_add=False)

    def __str__(self):
        return self.title

class comment(models.Model):
    post=models.ForeignKey(article,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    post_comment=models.TextField()

    def __str__(self):
        return self.post.title

class post(models.Model):
    post_author=models.ForeignKey(author,on_delete=models.CASCADE)
    body=RichTextUploadingField()

class post_comment(models.Model):
    comment=models.TextField()


class About(models.Model):
    u_name = models.ForeignKey(author, on_delete=models.CASCADE)
    Current_city = models.CharField(max_length=30)
    Home_town = models.CharField(max_length=30)
    School = models.CharField(max_length=50)
    University = models.CharField(max_length=50)
    Religion = models.CharField(max_length=30)
    Nationality = models.CharField(max_length=50)
    Meritial_status = models.CharField(max_length=30)
    Worked_at = models.CharField(max_length=100)

