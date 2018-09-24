from django.shortcuts import render,get_object_or_404
from .models import moview_details
from .serializers import MovieSerializer

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet

from django.http import Http404,JsonResponse,HttpResponse
import json,requests


@api_view(["POST"])
def mv_detail_titl(title_data):   #search movie by title
    title = (title_data.body).decode('UTF-8')
    try:
        title_data = moview_details.objects.filter(Title__icontains=title)
        if title_data.values()[0] is not None:
            return JsonResponse(title_data.values()[0], safe=False)
    except Exception as yt:
        print('not found in local db',yt)
        # var = 1
        dep_title = title.replace(' ','+')
        response = requests.get('http://www.omdbapi.com/?t=%s&type=movie&apikey=fe42ff19' % dep_title)
        geodata = response.json()


        new_movie, created = moview_details.objects.get_or_create(
            Title=geodata['Title'],
            # imdbID=geodata['imdbID'],
            Year=geodata['Year'],
            Genre=geodata['Genre'],
            Ratings=geodata['imdbRating']
        )
        if created:
            new_movie.save()

        return JsonResponse(geodata)

@api_view(["POST"])
def mv_detail_id(id_data):      #search movie by id ( if not found in db than it should IMDB id)
    id = (id_data.body).decode('UTF-8')
    try:
        id_data = moview_details.objects.filter(imdbID=id)

        if id_data.values()[0] is not None:
            return JsonResponse(id_data.values()[0], safe=False)
    except Exception as yt:
        print('not found in local db',yt)
        dep_title = id.replace(' ','+')
        response = requests.get('http://www.omdbapi.com/?i=%s&type=movie&apikey=fe42ff19' % dep_title)
        geodata = response.json()
        new_movie, created = moview_details.objects.get_or_create(
            Title=geodata['Title'],
            # imdbID=geodata['imdbID'],
            Year=geodata['Year'],
            Genre=geodata['Genre'],
            Ratings=geodata['imdbRating']
        )
        if created:
            new_movie.save()
        return JsonResponse(geodata)

@api_view(["POST"])
def mv_detail_year(year_data):          #search movie by year
    year = (year_data.body).decode('UTF-8')
    try:
        year_data = moview_details.objects.filter(Year=year)

        if year_data.values()[0] is not None:
            return JsonResponse(year_data.values()[0], safe=False)
    except Exception as yt:
        print('not found in local db',yt)
        dep_title = year.replace(' ','+')
        response = requests.get('http://www.omdbapi.com/?y=%s&type=movie&apikey=fe42ff19' % dep_title)
        geodata = response.json()
        new_movie, created = moview_details.objects.get_or_create(
            Title=geodata['Title'],
            # imdbID=geodata['imdbID'],
            Year=geodata['Year'],
            Genre=geodata['Genre'],
            Ratings=geodata['imdbRating']
        )
        if created:
            new_movie.save()
        return JsonResponse(geodata)

@api_view(["POST"])
def mv_detail_genre(genre_data):        #search movie by genre
    genre = (genre_data.body).decode('UTF-8')
    try:
        genre_data = moview_details.objects.filter(Genre__icontains=genre)

        json_posts = json.dumps(list(genre_data.values()))
        return JsonResponse(json_posts, safe=False)
    except Exception as yt:
        print('not found in local db',yt)
        dep_title = genre.replace(' ','+')
        response = requests.get('http://www.omdbapi.com/?g=%s&type=movie&apikey=fe42ff19' % dep_title)
        geodata = response.json()
        new_movie, created = moview_details.objects.get_or_create(
            Title=geodata['Title'],
            # imdbID=geodata['imdbID'],
            Year=geodata['Year'],
            Genre=geodata['Genre'],
            Ratings=geodata['imdbRating']
        )
        if created:
            new_movie.save()
        return JsonResponse(geodata)



class UpdateView(GenericAPIView, UpdateModelMixin):     # update data (Genre,Ratings) by id

    queryset = moview_details.objects.all()
    serializer_class = MovieSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
