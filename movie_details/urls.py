"""movie_details URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('title/', views.mv_detail_titl),
    path('id/', views.mv_detail_id),
    path('year/', views.mv_detail_year),
    path('genre/', views.mv_detail_genre),
    path('get_data/', views.get_data),
    # path('movies/', views.IndexView.as_view(), name='index'),

]
