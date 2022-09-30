from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.overview, name='overview'),
    path("api/get", views.all_posts, name='allposts'),
    path("api/get/<int:pk>", views.get_post, name='getpost'),
    path("api/post/", views.add_post, name='addpost'),
    path("api/delete/<pk>", views.delete_post, name='deletepost'),
]