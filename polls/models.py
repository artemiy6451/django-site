from django.db import models

# Create your models here.

class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

class Question(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choise(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
