from rest_framework import Response
from rest_framework import APIView
from .pusher import pusher_client


class MessageAPIView(APIView):
    def post(self, request):
        pusher_client.trigger('chat', 'message', {
            'username': request.data['username'],
            'message': request.data['message']
        })

        return Response([])
