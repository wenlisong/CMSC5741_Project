from django.conf.urls import url, include

from Similarity import views
from Similarity.views import index

urlpatterns = [
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^index/$', views.index, name='index')
]