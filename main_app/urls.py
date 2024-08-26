from django.urls import path, include
from . import views # Import views to connect routes to view functions
from django.contrib import admin

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
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
    path('themes/create/', views.ThemeCreate.as_view(), name='theme-create'),
    path('themes/<int:pk>/', views.ThemeDetail.as_view(), name='theme-detail'),
    path('themes/', views.ThemeList.as_view(), name='theme-index'),
    path('themes/<int:pk>/update/', views.ThemeUpdate.as_view(), name='theme-update'),
    path('themes/<int:pk>/delete/', views.ThemeDelete.as_view(), name='theme-delete'),
    path('researchpapers/<int:researchpaper_id>/associate-theme/<int:theme_id>/', views.associate_theme, name='associate-theme'),
    path('researchpapers/<int:researchpaper_id>/remove-theme/<int:theme_id>/', views.remove_theme, name='remove-theme'),
    path('accounts/signup/', views.signup, name='signup'),

]


