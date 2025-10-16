from django.db import models

class Movie(models.Model):
  name = models.CharField(max_length=255)
  genre = models.CharField(max_length=255)
  description = models.TextField()
  director = models.CharField(max_length=255)
  country = models.CharField(max_length=100)
  duration = models.FloatField()
  quality = models.CharField(max_length=50)
  release = models.IntegerField()
  rating = models.FloatField()
  category = models.IntegerField()
  link = models.URLField()
  imgUrl = models.URLField()

  def __str__(self):
    return self.name
