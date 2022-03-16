from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import *


urlpatterns = [
    path('<int:pk>', SelfProfile.as_view(), name='profile'),
    path('create/', register, name='create_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add_friend/', AddFriend.as_view(), name='add_friend'),
    path('add_friend/<int:user_id>', add_friend_by_id, name='add_friend_by_id'),
    path('friends/<int:user_id>', friend_list, name='friend_list'),
    path('update/profile/<int:pk>', UpdateProfile.as_view(), name='update_profile'),

    path('search/users/', SearchFriends.as_view(), name='search_users_result')
]