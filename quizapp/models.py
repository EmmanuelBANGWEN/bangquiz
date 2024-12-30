from django.db import models

#class Category(models.Model):
 #   name = models.CharField(max_length=100)

  #  def __str__(self):
  #      return self.name
    
class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    #category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User



class CustomUser(User):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    #email = models.CharField(max_length=100, blank=True, null=True)

    country = models.CharField(max_length=100, blank=True, null=True)

