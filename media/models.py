from django.db import models
from django.core.validators import MaxValueValidator

class user(models.Model):

    name=models.CharField(max_length=25)
    about=models.CharField(max_length=250)

class location(models.Model):
    name =models.CharField(max_length=200)
    shotname =models.CharField(max_length=200)
class Album(models.Model):
    title =models.CharField(max_length=200)
    view =models.CharField(max_length=200)
    Discription =models.CharField(max_length=200)
class tag(models.Model):
    
    title =models.CharField(max_length=200)
class tag_photo(models.Model):
    tagId =models.ForeignKey(tag,on_delete=models.CASCADE)
    photoID =models.CharField(max_length=200)
class comment(models.Model):
    photid =models.CharField(max_length=200)
    postdate =models.CharField(max_length=200)
    content =models.CharField(max_length=200)
class UserTofollow(models.Model):
    name =models.CharField(max_length=200)
    phonenumber =models.CharField(max_length=200)
    Email =models.CharField(max_length=200)
    Address =models.CharField(max_length=200)
class following(models.Model):
    use_id =models.ForeignKey(user, on_delete=models.CASCADE)
    followingId =models.CharField(max_length=200)
class photo(models.Model):

    AlbumID =models.ForeignKey(Album,on_delete=models.CASCADE)
    LocationId=models.ForeignKey(location,on_delete=models.CASCADE)
    MemberId=models.IntegerField(max_length=10)
    Title=models.CharField(max_length=200)
    Description=models.CharField(max_length=200)
    Privacy =models.CharField(max_length=200)
    UploaadDate=models.CharField(max_length=200)
    view= models.CharField(max_length=200)
    imagepathe =models.CharField(max_length=200)
