from django.urls import path

from blog.views import index, post_detail, post_new, post_edit

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_new, name='post_new'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
]