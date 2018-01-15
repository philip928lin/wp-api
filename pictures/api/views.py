# movies-api/movies/api/views.py

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import Picture
from api.serializers import PictureSerializer


class PictureCreateView(ListCreateAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer