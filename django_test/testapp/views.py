from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from testapp.appserilizer import UserSerializer, InformationSerializer
from testapp.models import User, Information


class UserViwSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all().order_by('id')
    serializer_class = InformationSerializer