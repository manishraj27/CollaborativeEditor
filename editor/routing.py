from django.urls import path
from editor import consumers

websocket_urlpatterns = [
    path('ws/messages/<str:room_id>/<str:username>/', consumers.ChatConsumer.as_asgi()),
]
