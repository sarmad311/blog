from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('create-service/', views.create_service, name='create_service'),
    path('services/', views.all_services, name='all_services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name="contact"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)