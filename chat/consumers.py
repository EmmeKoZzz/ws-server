import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        roomName = self.scope["path_remaining"]
        print(self.scope)
        self.accept();
        self.send(text_data=json.dumps({
            'type':'connected',
            'payload': 'Successful Conection.',
        }))