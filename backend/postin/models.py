from django.db import models


    
    
class User(models.Model):
    nickname = models.CharField(max_length=100)
    
    def serialize(self):
        return {
            "nickname" : self.nickname
        }
    
    
    
# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def serialize(self):
        return {
            "id" : self.id,
            "tittle" : self.tittle,
            "content": self.content,
            "author" : self.author.nickname
        }