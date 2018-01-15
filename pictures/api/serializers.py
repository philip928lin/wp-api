# movies-api/movies/api/serializers.py

from rest_framework.serializers import ModelSerializer

from api.models import Picture

class PictureSerializer(ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id', 'created', 'last_modify_date', 'like_count', 'tags')
        extra_kwargs = {
            'id': {'read_only': True}
        }