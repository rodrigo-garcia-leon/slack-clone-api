"""
ASGI config for slack_clone project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.middleware import BaseMiddleware
from channels.db import database_sync_to_async
from django.core.asgi import get_asgi_application
from django.contrib.auth.models import AnonymousUser
from rest_framework.authtoken.models import Token
from chat_groups_api.apps.core.routing import websocket_urlpatterns


@database_sync_to_async
def get_user(token_key):
    try:
        token = Token.objects.get(key=token_key.decode())
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()

class TokenAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        scope = dict(scope)
        token_key = scope["query_string"]
        scope['user'] = await get_user(token_key)

        return await self.inner(scope, receive, send)


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": TokenAuthMiddleware(URLRouter(websocket_urlpatterns))
})
