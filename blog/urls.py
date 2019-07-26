from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('article-<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('create/', views.PostCreateView.as_view(), name='post-create'),
    path('', views.PostListView.as_view(), name='posts'),
]
