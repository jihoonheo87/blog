from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views
urlpatterns = [
    # path('',views.home, name='blog-home'),
    path('',PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete'), #post_confirm_delete.html
    path('post/new/',PostCreateView.as_view(), name='post-create'), #post_form.html
    path('about/',views.about, name='blog-about'),
]