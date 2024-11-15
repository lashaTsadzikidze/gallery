import django_filters
from gallery.models import Artwork

class ArtworkFilter(django_filters.FilterSet):
    class Meta:
        model = Artwork
        fields = ['artist', 'created_at']