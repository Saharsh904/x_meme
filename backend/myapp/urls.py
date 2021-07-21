from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('memes', views.meme_list),
    path('memes/<int:pk>/', views.meme_detail),
]
