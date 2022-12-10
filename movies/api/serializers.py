from rest_framework import serializers

from movies.models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'release_date', 'avatar')
        extra_kwargs = {'avatar': {'required': False}, 'description': {'required': False}}

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance
    #     return super().update(instance, validated_data)






