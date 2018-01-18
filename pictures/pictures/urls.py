from django.conf.urls import url, include # add include as an import here
from django.contrib import admin
from rest_framework import routers
from api import views
router = routers.DefaultRouter()
router.register(r'pics', views.PictureViewSet)
router.register(r'features', views.FeatureViewSet)
router.register(r'votes', views.VoteRecordViewSet)


# router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    # url(r'^api/', include('api.urls')) # add this line
    
]