from django.db import models
from django.core.validators import MaxValueValidator

class user(models.Model):
    firstname=models.CharField(max_length=25, null=True)
    lastname=models.CharField(max_length=250,null=True)
    email= models.CharField(max_length=200,null=True)
    profile =models.FileField(null=True,blank=True)
   
   

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
class following(models.Model):
   
    use_id =models.ForeignKey(user, on_delete=models.CASCADE)
    followingId =models.CharField(max_length=200)
class UserTofollow(models.Model):
    following = models.ManyToManyField(following)
    name =models.CharField(max_length=200)
    phonenumber =models.CharField(max_length=200)
    Email =models.CharField(max_length=200)
    Address =models.CharField(max_length=200)

class photo(models.Model):
    user = models.ManyToManyField(user)
    location = models.ManyToManyField(location)
    Album = models.ManyToManyField(Album)
    MemberId=models.IntegerField( validators=[MaxValueValidator(9999999999)])
    Title=models.CharField(max_length=200)
    Description=models.CharField(max_length=200)
    Privacy =models.CharField(max_length=200)
    UploaadDate=models.CharField(max_length=200)
    view= models.CharField(max_length=200)
    songs = models.CharField(max_length=200,null=True)
    imagepathe =models.FileField(null=True,blank=True)

    def __str__(self):
        return self.Title

class comment(models.Model):
    photo = models.ManyToManyField(photo)
    tag = models.ManyToManyField(tag)
    photid =models.CharField(max_length=200)
    postdate =models.CharField(max_length=200)
    content =models.CharField(max_length=200)
