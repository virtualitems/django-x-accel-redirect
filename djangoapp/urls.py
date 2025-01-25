"""
URL configuration for djangoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

MEDIA_DIRECTORY = '/home/app1user/djangoapp/media'

def protected_media(request, filename):
    import os
    import mimetypes
    from django.http import HttpResponse

    file_path = os.path.join(MEDIA_DIRECTORY, filename)
    if not os.path.isfile(file_path):
        return HttpResponse("File not found", status=404)

    mime_type, encoding = mimetypes.guess_type(filename)

    response = HttpResponse()
    response['Cache-Control'] = 'no-cache'
    response['Content-Type'] = mime_type
    response['X-Accel-Redirect'] = f'/media-chest/{filename}'
    return response

def hello(req):
    from django.http import HttpResponse
    return HttpResponse('welcome!')

urlpatterns = [
    path('', hello),
    path('media/<str:filename>', protected_media),
    path('admin/', admin.site.urls),
]
