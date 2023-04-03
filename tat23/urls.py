from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from tat23 import views

urlpatterns = [
    re_path(r'^mail$', views.send_email),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
