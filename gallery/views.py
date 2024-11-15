from rest_framework import viewsets, views
from gallery.models import Artist, Artwork, Exhibition
from gallery.serializers import ArtistSerializer, ArtworkSerializer, ExhibitionSerializer
from gallery.permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from gallery.filters import ArtworkFilter

# Create your views here.
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]

class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    filterset_class = ArtworkFilter

class ExhibitionViewSet(viewsets.ModelViewSet):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionSerializer
    permission_classes = [IsAdminOrReadOnly]