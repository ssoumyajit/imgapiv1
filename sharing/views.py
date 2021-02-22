from django.shortcuts import render

from django.shortcuts import render
from .models import Sharing, Comments, LikesToSharing
from rest_framework import viewsets
from .serializers import SharingSerializers, CommentSerializers, LikesToSharingSerializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication


class SharingViewSets(viewsets.ModelViewSet):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['s_teacher__name', 's_student__name']
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class LikesToSharingViewSets(viewsets.ModelViewSet):
    # here it does not make sense to list all the likes at one place,
    # rather make the queryset specific to an instance of sharing, same for comments also.
    queryset = LikesToSharing.objects.all()
    serializer_class = LikesToSharingSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['l_shareid__id']
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['c_shareid__id']
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticatedOrReadOnly,)

