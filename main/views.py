from django.shortcuts import render
from django.http import FileResponse, HttpResponseNotFound
import os
from django.conf import settings

def serve_manual(request):
    try:
        file_path = os.path.join(settings.BASE_DIR, 'static', 'pdfs', '2025GameManual.pdf')
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    except Exception as e:
        print(f"Error serving manual: {e}")
        return HttpResponseNotFound('Unable to access game manual')

def home(request):
    return render(request, 'main/home.html')

def pit_scout(request):
    return render(request, 'main/pit_scout.html')

def serve_thumbnail(request):
    try:
        thumbnail_path = r'C:\Users\yello\Downloads\gamemanual\reefscapethumbnail'
        return FileResponse(open(thumbnail_path, 'rb'), content_type='image/jpeg')  # Adjust content type if needed
    except Exception as e:
        print(f"Error serving thumbnail: {e}")
        return HttpResponseNotFound('Unable to access thumbnail')