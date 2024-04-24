from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'job_listing_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_job, name='upload'),
    path('apply_job/<int:job_id>/', views.apply_job, name='apply_job'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
