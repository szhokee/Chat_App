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


# api/create_delete_chat/<int:user1_id>/<int:user2_id> - создание или удаление чата между пользователями с идентификаторами user1_id и user2_id
# api/get_threads/<int:user_id> - получение списка чатов пользователя с идентификатором user_id
# api/get_create_message/<int:thread_id> - получение и создание сообщений в чате с идентификатором thread_id
# api/set_message_status - изменение статуса сообщения в чате
# api/count_unread_message/<int:user_id> - получение количества непрочитанных сообщений пользователя с идентификатором user_id
#