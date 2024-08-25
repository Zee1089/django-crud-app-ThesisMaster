from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('researchpapers/', views.researchpaper_index, name='researchpaper-index'),
    path('researchpapers/<int:researchpaper_id>/', views.researchpaper_detail, name='researchpaper-detail'),
    path('researchpapers/<int:researchpaper_id>/', views.researchpaper_detail, name='researchpaper-detail'),
]

