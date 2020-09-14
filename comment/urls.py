from django.urls import path
from . import views

urlpatterns = [
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]
