# cv/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # When someone visits the root of our app, show the cv_view
    path('', views.cv_view, name='cv-view'),
]