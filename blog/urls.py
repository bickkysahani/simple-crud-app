from django.urls import path
from .views import blogs,  blog_detail, blog_create, blog_update, blog_delete

urlpatterns = [
    path('', blogs, name='blogs'),
    path('blogs/<int:blog_id>/', blog_detail, name='blog_detail'), 
    path('blogs/blog_create/', blog_create, name='blog_create'),
    path('blogs/<int:id>/edit/',blog_update , name='blog_edit'),
    path('blogs/<int:id>/delete/', blog_delete, name='blog_delete'),
]
