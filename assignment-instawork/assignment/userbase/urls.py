from django.conf.urls import url, include
from rest_framework import routers
from views import UsersViewSet


itemrouter = routers.DefaultRouter(trailing_slash=False)
itemrouter.register(r'users', UsersViewSet, base_name='items')
urlpatterns = [
    url(r'', include(itemrouter.urls)),
]