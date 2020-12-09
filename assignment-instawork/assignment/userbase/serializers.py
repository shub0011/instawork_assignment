from rest_framework import serializers
from django.db import models
from models import Users
ROLES = (
    ('A', 'Admin'),
    ('R', 'Regular'),
)


class UserSerializer(serializers.ModelSerializer):
    first_name = models.CharField( max_length=30)
    last_name = models.CharField( max_length=30, blank=True)
    email = models.EmailField( unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(
        max_length=1, null=True, blank=True, choices=ROLES)
    resource_url = serializers.SerializerMethodField()

    class Meta:
        model = Users
        fields = ('id','first_name', 'last_name', 'phone_number', 'email',
                  'role', 'resource_url')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        return user

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance, validated_data)
        return user

    def destroy(self, instance, validated_data):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_resource_url(self, obj):
        request = self.context.get('request')
        if self.context['view'].kwargs.get('pk'):
            return request.build_absolute_uri()
        return request.build_absolute_uri('users' + '/{id}'.format(
            id=obj.id))