from django.shortcuts import render
from .models import moview_details
from .serializers import MovieSerializer

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404,JsonResponse,HttpResponse
from django.core import serializers
from django.conf import settings
import json,requests,omdb
from django.core import serializers


@api_view(["POST"])
def mv_detail_titl(title_data):
    title = (title_data.body).decode('UTF-8')
    var = 0
    try:
        title_data = moview_details.objects.filter(Title__icontains=title)
        # print('data from local',title_data.values())
        # print('data from local',title_data.values()[0])
        # print('data from local',title_data.values()[0]['Title'])
        if title_data.values()[0] is not None:
            # print('found from local', title_data.values()[0])
            return JsonResponse(title_data.values()[0], safe=False)
    except Exception as yt:
        # print('not found in local db',yt)
        # var = 1
        dep_title = title.replace(' ','+')
        response = requests.get('http://www.omdbapi.com/?t=%s&type=movie&apikey=fe42ff19' % dep_title)
        geodata = response.json()
        return JsonResponse(geodata)

@api_view(["POST"])
def mv_detail_id(id_data):
    # print('\ntitle data:%s\n' % (title_data.body).decode("utf-8"))
    id = (id_data.body).decode('UTF-8')
    try:
        id_data = moview_details.objects.filter(imdbID=id)
        # print('data from local',title_data.values())
        # print('data from local',title_data.values()[0])
        # print('data from local',title_data.values()[0]['Title'])
        if id_data.values()[0] is not None:
            # print('found from local', title_data.values()[0])
            return JsonResponse(id_data.values()[0], safe=False)
    except Exception as yt:
        # print('not found in local db',yt)
        dep_title = id.replace(' ','+')
        response = requests.get('http://www.omdbapi.com/?i=%s&type=movie&apikey=fe42ff19' % dep_title)
        geodata = response.json()
        return JsonResponse(geodata)

@api_view(["POST"])
def mv_detail_year(year_data):
    # print('\ntitle data:%s\n' % (title_data.body).decode("utf-8"))
    year = (year_data.body).decode('UTF-8')
    try:
        year_data = moview_details.objects.filter(Year=year)
        # print('data from local',title_data.values())
        # print('data from local',title_data.values()[0])
        # print('data from local',title_data.values()[0]['Title'])
        if year_data.values()[0] is not None:
            # print('found from local', title_data.values()[0])
            return JsonResponse(year_data.values()[0], safe=False)
    except Exception as yt:
        # print('not found in local db',yt)
        dep_title = year.replace(' ','+')
        response = requests.get('http://www.omdbapi.com/?y=%s&type=movie&apikey=fe42ff19' % dep_title)
        geodata = response.json()
        return JsonResponse(geodata)

@api_view(["POST"])
def mv_detail_genre(genre_data):
    # print('\ntitle data:%s\n' % (title_data.body).decode("utf-8"))
    genre = (genre_data.body).decode('UTF-8')
    try:
        genre_data = moview_details.objects.filter(Genre__icontains=genre)
        # print('data from local',genre_data.values())
        # print('data from local',genre_data.values()[0])
        # print('data from local',genre_data.values()[0]['Title'])
        json_posts = json.dumps(list(genre_data.values()))
        # print("json",json_posts)
        return JsonResponse(json_posts, safe=False)
    except Exception as yt:
        # print('not found in local db',yt)
        dep_title = genre.replace(' ','+')
        response = requests.get('http://www.omdbapi.com/?g=%s&type=movie&apikey=fe42ff19' % dep_title)
        geodata = response.json()
        return JsonResponse(geodata)


@api_view(["POST"])
def get_data(da_data):
    try:
        data=json.loads(da_data.body)
        return JsonResponse("This will be the data:"+data+"",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
