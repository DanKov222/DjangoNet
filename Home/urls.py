from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create/post', CreateLocalPost.as_view(), name='create_local_post'),
    path('update/post/<int:pk>', UpdateLocalPost.as_view(), name='update_local_post'),
    path('delete/post/<int:pk>', DeleteLocalPost.as_view(), name='delete_local_post'),

    path('add/like/<int:post_id>', add_like, name='add_like'),
    path('post/<int:pk>', DetailLocalPost.as_view(), name='local_detail'),
    path('add/comment/<int:post_id>', add_comment, name='comment')
]