from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import  permissions, generics, mixins
from .models import Channel, Message
from .serializers import UserSerializer, ChannelSerializer, MessageSerializer

def index(_):
    return HttpResponse()

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChannelList(generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(users__id=self.request.user.id)

class MessageList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    channel_id = None

    def get(self, request, *args, **kwargs):
        self.channel_id = kwargs['channel_id']

        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        return self.queryset.filter(channel_id=self.channel_id)