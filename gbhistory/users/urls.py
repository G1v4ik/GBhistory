from django.urls import path

from .views import users_index, UserRegisterView,\
UserLoginView, UserLogoutView, user_info

urlpatterns = [
    path('', users_index, name='profile_index'),
    path('reg/', UserRegisterView.as_view(), name='profile_register'),
    path('login/', UserLoginView.as_view(), name='profile_login'),
    path('logout/', UserLogoutView.as_view(), name='profile_logout'),
    path('info/<int:id>', user_info, name='user_info')
]
