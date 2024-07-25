from django.urls import path
from . views import index, upload_video, download_video

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload_video, name='upload_video'),
    path('download/', download_video, name='download_video'),
]
