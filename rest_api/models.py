from django.db import models

# Create your models here.

class moview_details(models.Model):
    imdbID = models.AutoField(primary_key=True,unique=True)
    Title = models.CharField(max_length=250)
    Year = models.IntegerField()
    # Rated = models.CharField(max_length=250)
    # Released = models.CharField(max_length=15)
    # Runtime = models.CharField(max_length=15)
    Genre = models.TextField()
    # Director = models.CharField(max_length=250)
    # Writer = models.TextField()
    # Actors = models.TextField()
    # Plot = models.TextField()
    # Language = models.CharField(max_length=250)
    # Country = models.CharField(max_length=250)
    # Awards = models.TextField()
    # Poster = models.TextField()
    Ratings = models.CharField(max_length=6)
    # Metascore = models.IntegerField()
    # imdbRating = models.FloatField()
    # imdbVotes = models.IntegerField()
    # Type = models.CharField(max_length=20)
    # DVD = models.CharField(max_length=15)
    # BoxOffice = models.CharField(max_length=250)
    # Production = models.CharField(max_length=250)
    # Website = models.CharField(max_length=250)
    # Response = models.CharField(max_length=25)

