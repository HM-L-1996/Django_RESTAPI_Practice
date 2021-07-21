
from django.conf.urls import url, include
from django.contrib import admin

from rest_api.views import tutorial_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('rest_api.urls')),
]