from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    # path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('researchpapers/', views.researchpaper_index, name='researchpaper-index'),
    path('researchpapers/<int:researchpaper_id>/', views.researchpaper_detail, name='researchpaper-detail'),
    path('researchpapers/<int:researchpaper_id>/', views.researchpaper_detail, name='researchpaper-detail'),
    path('researchpapers/create/', views.ResearchPaperCreate.as_view(), name='researchpaper-create'),
    path('researchpapers/<int:pk>/update/', views.ResearchPaperUpdate.as_view(), name='researchpaper-update'),
    path('researchpapers/<int:pk>/delete/', views.ResearchPaperDelete.as_view(), name='researchpaper-delete'),
    path(
        'researchpapers/<int:researchpaper_id>/add-comment/', 
        views.add_comment, 
        name='add-comment'
    ),
]

