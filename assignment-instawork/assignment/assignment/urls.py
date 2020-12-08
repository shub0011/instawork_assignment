
from rest_framework import routers
from django.contrib import admin
from django.conf.urls import patterns, include, url

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    
]
