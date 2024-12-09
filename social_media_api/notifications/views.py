from django.shortcuts import render

# Create your views here.


# notifications/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification

class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, is_read=False)
        notifications_data = [{
            'actor': notification.actor.username,
            'verb': notification.verb,
            'timestamp': notification.timestamp
        } for notification in notifications]

        return Response(notifications_data)





class MarkNotificationAsReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, notification_id):
        notification = Notification.objects.get(id=notification_id, recipient=request.user)
        notification.is_read = True
        notification.save()
        return Response({'detail': 'Notification marked as read.'})
