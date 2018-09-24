from rest_framework import serializers
from .models import moview_details


class MovieSerializer(serializers.ModelSerializer):


    class Meta:
        model = moview_details
        fields = ('Genre', 'Ratings')
