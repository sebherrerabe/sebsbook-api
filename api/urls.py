from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='home'),
    path('posts/', views.handle_posts, name='posts'),
    path('posts/<uuid:pk>', views.handle_post, name='post'),
]