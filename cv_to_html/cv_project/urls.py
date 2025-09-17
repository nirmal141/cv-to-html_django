"""
Main URL configuration for cv_project.
Simplified to only include CV app routes.
"""

from django.urls import path, include

urlpatterns = [
    path('', include('cv.urls')),  # Include CV app URLs
]