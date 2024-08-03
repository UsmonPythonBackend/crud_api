from django.urls import path
from .views import ArtistAPIView, ArtistAPIViewMobile, AlbomAPIView, SongAPIView, SongDetailAPIView, \
    ArtistDetailAPIView, AlbomDetailAPIView

urlpatterns = [
    path('artist/', ArtistAPIView.as_view(), name='artist'),
    path('artist-mobile/', ArtistAPIViewMobile.as_view(), name='artist-mobile'),
    path('albom/', AlbomAPIView.as_view(), name='album'),
    path('songs/', SongAPIView.as_view(), name='songs'),
    path('songs/<int:id>/', SongDetailAPIView.as_view(), name='song-detail'),
    path('artist/<int:id>/', ArtistDetailAPIView.as_view(), name='artist-detail'),
    path('albom/<int:id>/', AlbomDetailAPIView.as_view(), name='albom-detail'),
]