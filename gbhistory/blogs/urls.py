from django.urls import path
from .views import post_of_theme, post_detail,\
AddPostView, post_my

app_name = 'blogs'

urlpatterns = [
    path('theme/<slug:slug_theme>', post_of_theme, name='theme'),
    path('theme/<slug:slug_theme>/<slug:slug_post>', post_detail, name='post'),
    path('post_add/', AddPostView.as_view(), name='post_add'),
    path('posts/user/<int:user_id>', post_my, name='post_my'),
]
