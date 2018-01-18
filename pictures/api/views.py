# movies-api/movies/api/views.py

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from api.models import Picture, VoteRecord, Feature
from api.serializers import PictureSerializer, VoteRecordSerializer, FeatureSerializer


# class PictureCreateView(ListCreateAPIView):
#     queryset = Picture.objects.all()
#     serializer_class = PictureSerializer

# class PictureDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Picture.objects.all()
#     serializer_class = PictureSerializer

# class FeatureCreateView(ListCreateAPIView):
#     queryset = Feature.objects.all()
#     serializer_class = FeatureSerializer

# class FeatureDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Feature.objects.all()
#     serializer_class = FeatureSerializer

# class VoteRecordCreateView(ListCreateAPIView):
#     queryset = VoteRecord.objects.all()
#     serializer_class = VoteSerializer

# class VoteRecordDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = VoteRecord.objects.all()
#     serializer_class = VoteSerializer

class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    
class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer

class VoteRecordViewSet(viewsets.ModelViewSet):
    queryset = VoteRecord.objects.all()
    serializer_class = VoteRecordSerializer 
    