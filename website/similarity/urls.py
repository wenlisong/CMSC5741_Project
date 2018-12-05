from django.urls import path, include

from similarity import views

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('index/', views.index, name='index'),
]