from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.TextField()
    def __str__(self) :
        return f'Message from {self.name}'
  
#uploading profile info code changes      
class Post(models.Model):
	#pfp=models.ImageField(null=True, blank=True, upload_to='images/')
	#file = models.FileField()
	name=models.CharField(max_length=30)
	pron=models.CharField(max_length=15)
	desc=models.TextField()
	gymLocations=models.TextField(max_length=50)
	climbType=models.TextField(max_length=50)
	expLevel=models.TextField(max_length=15)
	availability=models.TextField(max_length=20)
	username=models.TextField(max_length=40)
	#skills=models.TextField(max_length=50)
	def __str__(self) :
		return f'{self.name}s Profile'

class FilesUpload(models.Model):
    file = models.FileField()
    
class Comment(models.Model):
    name=models.CharField(max_length=30)
    subject=models.TextField()
    def __str__(self) :
        return f'Comment from {self.name}'
    
class Matches(models.Model):
    user=models.TextField(max_length=50)
    matches=models.TextField(max_length=100)
    def __str__(self) :
        return f'Matches Selections for {self.user}'