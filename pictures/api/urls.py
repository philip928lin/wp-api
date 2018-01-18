from django.conf.urls import url

from api.views import PictureCreateView, PictureDetailView, FeatureCreateView,\
 FeatureDetailView, VoteRecordCreateView, VoteRecordDetailView


urlpatterns = [
    url(r'^pictures/$', PictureCreateView.as_view(), name='pictures'),
    url(r'^pictures/(?P<id>[0-9]+)$', PictureDetailView.as_view(), name='detail'),
    url(r'^features/$', FeatureCreateView.as_view(), name='features'),
    url(r'^features/(?P<id>[0-9]+)$', FeatureDetailView.as_view(), name='features_details'),
    
    url(r'^votes/$', VoteRecordCreateView.as_view(), name='votes'),
    url(r'^votes/(?P<id>[0-9]+)$', VoteRecordDetailView.as_view(), name='votes_details'),
    
] 