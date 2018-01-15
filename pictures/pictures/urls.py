from django.conf.urls import url, include # add include as an import here
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')) # add this line
]