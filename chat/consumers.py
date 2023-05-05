import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        roomName = self.scope["url_route"]["kwargs"]
        self.accept();
        self.send(text_data=json.dumps({
            'type':'connected',
            'msessage': 'well done!',
            'room': roomName
        }))