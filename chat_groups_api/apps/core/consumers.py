from datetime import datetime
import json
from asgiref.sync import sync_to_async
from django.utils.timezone import make_aware
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Channel
from .serializers import MessageSerializer

class ChannelConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        channel_id = self.scope["url_route"]["kwargs"]["channel_id"]
        self.channel = await sync_to_async(Channel.objects.get)(id=channel_id)

        await self.accept()
        await self.channel_layer.group_add(self.channel.name, self.channel_name)

    async def disconnect(self, _):
        await self.channel_layer.group_discard(self.channel.name, self.channel_name)

    async def receive(self, text_data):
        user = self.scope['user']

        text_data_json = json.loads(text_data)
        content = text_data_json['message']

        message = Message(**{
            "user": user,
            "channel": self.channel,
            "content": content,
            "created": make_aware(datetime.now())
        })
        await sync_to_async(message.save)()

        serializer = MessageSerializer(message)

        await self.channel_layer.group_send(self.channel.name, {
            'type': 'channel.message',
            'data': serializer.data
        })

    async def channel_message(self, event):
        data = event['data']

        await self.send(text_data=json.dumps({
            'content': data['content'],
            "username": data['username'],
            "created": data['created']
        }))
