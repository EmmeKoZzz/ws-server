import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        roomName = self.scope["path_remaining"]
        self.accept();
        self.send(text_data=json.dumps({
            'type':'connected',
            'payload': 'Successful Conection.',
        }))

    def receive(self, text_data):
        data = json.loads(text_data)
        payload = data['payload']
        self.send(text_data=json.dumps({
            'type': "chatMessage",
            'payload': f'{payload} recived!'
        })) 

    def disconnect(self, code):
        pass
        