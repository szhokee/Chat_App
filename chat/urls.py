from django.contrib import admin
from django.urls import path, re_path
from chat.views import *


urlpatterns = [
    re_path(r'^api/create_delete_chat/(?P<user1_id>\d+)/(?P<user2_id>\d+)$',
            CreateDeleteThreads.as_view(), name='create_delete_chat'),
    re_path(r'^api/get_threads/(?P<user_id>\d+)$', GetThreads.as_view(), name='get_threads'),
    re_path(r'^api/get_create_message/(?P<thread_id>\d+)$', GetCreateMessage.as_view(), name='get_create_message'),
    path('api/set_message_status', SetMessageStatus.as_view(), name='set_message_status'),
    re_path(r'^api/count_unread_message/(?P<user_id>\d+)$', CountUnreadMessage.as_view(), name='count_unread_message'),
]
