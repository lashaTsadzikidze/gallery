from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gallery import views

router = DefaultRouter()

router.register(r'artists', views.ArtistViewSet)
router.register(r'artworks', views.ArtworkViewSet)
router.register(r'exhibitions', views.ExhibitionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]