from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification


class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = request.user.Notification.filter(read=False).order_by('-created_at')
        data = [{
            'id': notification.id,
            'actor': notification.actor.username,
            'verb': notification.verb,
            'target': str(notification.target),
            'created_at': notification.created_at
        } for notification in notifications]
        return Response(data)
