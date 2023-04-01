from django.db.models import Count
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from chat.serializers import *
from chat.pagination import *
from rest_framework.permissions import IsAuthenticated


class CreateDeleteThreads(APIView):
    serializer_class = ThreadsSerializers
    permission_classes = [IsAuthenticated]

    def post(self, request, user1_id, user2_id):
        thread = Thread.objects.filter(participants__in=[user1_id, user2_id]).\
            annotate(num_participants=Count('participants')).filter(num_participants=2).first()

        if thread:
            serializer = self.serializer_class(thread)
            return Response({
                'results': 'Thread already exist',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        else:
            user1_obj = User.objects.get(pk=user1_id)
            user2_obj = User.objects.get(pk=user2_id)

            thread = Thread.objects.create()
            thread.participants.add(user1_obj, user2_obj)

            serializer = self.serializer_class(thread)
            return Response({
                'results': 'Thread successfully created',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

    def delete(self, request, user1, user2):
        thread = Thread.objects.filter(participants__in=[user1, user2]).\
            annotate(num_participants=Count('participants')).filter(num_participants=2).first()

        if thread:
            thread.delete()
            return Response({'results': 'Thread successfully deleted'}, status=status.HTTP_200_OK)
        else:
            return Response({'results': 'object does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class GetThreads(ListAPIView):
    serializer_class = ThreadsSerializers
    pagination_class = ThreadsPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.kwargs['user_id']
        threads = Thread.objects.filter(participants__id=user).order_by('-updated')

        for thread in threads:
            last_message = thread.messages.last()
            thread.last_message = last_message

        return threads


class GetCreateMessage(APIView):
    serializer_class = MessageSerializer
    pagination_class = ThreadsPagination
    permission_classes = [IsAuthenticated]

    def get(self, request, thread_id):
        messages = Message.objects.filter(thread_id=thread_id)
        paginator = self.pagination_class()
        paginated_messages = paginator.paginate_queryset(messages, request)
        serializer = self.serializer_class(paginated_messages, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, thread_id):
        sender = request.data.get('sender')
        text = request.data.get('message_text')

        if not text:
            return Response({'error': 'Text is required'}, status=status.HTTP_400_BAD_REQUEST)

        message = Message.objects.create(thread_id=thread_id, text=text, sender_id=sender)
        serializer = MessageSerializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SetMessageStatus(APIView):
    pagination_class = ThreadsPagination
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message_id = request.data.get('message_id', [])
        if not message_id:
            return Response({'result': 'error', 'message': 'No message IDs provided'},
                            status=status.HTTP_400_BAD_REQUEST)

        messages = Message.objects.filter(id__in=message_id)
        messages.update(is_read=True)

        return Response({'result': 'success', 'messages': messages.values()}, status=status.HTTP_200_OK)


class CountUnreadMessage(ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        user_id = self.kwargs['user_id']
        queryset = Message.objects.filter(sender__pk=user_id, is_read=False)
        return queryset

    def list(self, request, *args, **kwargs):
        count_queryset = len(self.get_queryset())
        return Response({'Amount of unread messages for this user': count_queryset}, status=status.HTTP_200_OK)
