from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/create/', views.blog_create, name='blog_create'),
    path('create-service/', views.create_service, name='create_service'),
    path('services/', views.all_services, name='all_services'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)