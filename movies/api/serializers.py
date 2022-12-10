from rest_framework import serializers

from movies.models import *


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'avatar', 'genres')
        extra_kwargs = {'avatar': {'required': False}, 'genres': {'required': False}}





