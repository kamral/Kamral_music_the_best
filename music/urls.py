from .views import MusicView,\
    MusicDetailView, \
    MusicDeleteView,\
    MusicUpdateView,\
    MusicCreateView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import  static

urlpatterns=[
    path('', MusicView.as_view(), name='music_list'),
    path('<int:pk>/',  MusicDetailView.as_view(), name='music_detail'),
    path('<int:pk>/edit/', MusicUpdateView.as_view(), name='music_edit'),
    path('<int:pk>/delete/', MusicDeleteView.as_view(), name='music_delete'),
    path('new/', MusicCreateView.as_view(), name='music_new'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)