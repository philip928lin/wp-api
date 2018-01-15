from django.conf.urls import url

from api.views import PictureCreateView, PictureDetailView

urlpatterns = [
    url(r'^pictures/$', PictureCreateView.as_view(), name='pictures'),
    url(r'^pictures/(?P<id>[0-9]+)$', PictureDetailView.as_view(), name='detail'),
]