import os
from typing import Union

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from . utils import perform_predictions


def index(request):
    return render(request, 'index.html')


def upload_video(request):
    if request.method == 'POST' and request.FILES['video']:
        uploaded_file = request.FILES['video']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        video_path: Union[str, bytes] = fs.path(filename)
        output_path = fs.path('output.mp4')  # Change this as needed
        perform_predictions(video_path, output_path)  # Call function to perform predictions
        os.remove(video_path)
        return render(request, 'index.html', {'output_file_url': fs.url('output.mp4')})
    return render(request, 'index.html')


def download_video(request):
    if request.method == 'POST':
        filename = 'output.mp4'  # Change this as needed
        filepath = f'{filename}'  # Update the path to your output file
        with open(filepath, 'rb') as f:
            response = HttpResponse(f.read(), content_type="video/mp4")
            response['Content-Disposition'] = f'attachment; filename={filename}'
            return response
    return HttpResponse(status=400)
