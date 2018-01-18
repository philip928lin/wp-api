# movies-api/movies/api/serializers.py

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from api.models import Picture, VoteRecord, Feature

class PictureSerializer(ModelSerializer):
    images_id = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Picture
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }
class FeatureSerializer(ModelSerializer):
    features_id =serializers.StringRelatedField(many=True)

    class Meta:
        model = Feature
        fields = '__all__'
        
class VoteRecordSerializer(ModelSerializer):
    # images_id = serializers.StringRelatedField(many=True)
    # features_id = serializers.StringRelatedField(many=True)

    class Meta:
        model = VoteRecord
        # fields = ('id', 'user_id', 'is_voted', 'created_at', 'images_id', 'features_id')
        fields = '__all__'
        
