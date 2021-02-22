from django.shortcuts import render
from .models import Artist, ArtistData, Highlights, Journey
from .serializers import ArtistSerializers, ArtistDataSerializers, HighlightsSerializers, JourneySerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import permissions
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOrReadonly
from rest_framework import generics


class ArtistListCreateViews(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

    # filtering which artists to be shown
    # may be filter using dance style, teachers later
    """
        def get_queryset(self):
        # Filter active products
            return Product.objects.filter(active=True)
    """


class ArtistRetrieveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    # retrieve stands for read-only endpoints to represent a single model instance.
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers
    lookup_field = "username__name"
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)   # uses the id field of user object, it seems.


class ArtistDataCreateViews(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistDataSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ArtistDataRetrieveUpdateDestroyViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtistData.objects.all()
    serializer_class = ArtistDataSerializers
    lookup_field = 'username__name'
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class HighlightsListCreateViews(generics.ListCreateAPIView):
    queryset = Highlights.objects.all()
    serializer_class = HighlightsSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['username__name']
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # just use explicit queryset n filter


class HighlightsRUDViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Highlights.objects.all()
    serializer_class = HighlightsSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)
    # lookup_field - using instance id.

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class JourneyListCreateViews(generics.ListCreateAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['username__name']
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class JourneyRUDViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializers
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadonly,)

    # lookup_field - using instance id.

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)