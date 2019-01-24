from rest_framework import serializers

from testapp.models import User, Information


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =('user','name')

class InformationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Information
        fields =('city','id')