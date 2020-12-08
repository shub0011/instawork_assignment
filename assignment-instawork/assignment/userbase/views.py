from userbase.serializers import UserSerializer
from userbase.models import Users
from rest_framework.decorators import detail_route
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render



class UsersViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):

        users = Users.objects.all()
        return users

    def get(self, request):
        users = self.get_queryset()
        results = {'data': users}
        return Response(results, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        super(UsersViewSet, self).perform_create(serializer)
        users = serializer.instance
        return users

    def perform_update(self, serializer):
        super(UsersViewSet, self).perform_update(serializer)
        users = serializer.instance
        return users

    def perform_destroy(self, serializer):
        super(UsersViewSet, self).perform_destroy(serializer)
        return None