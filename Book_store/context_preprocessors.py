from django.urls import reverse

def get_current_path(request):
    return {'path': request.path}