import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync as ats

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room = self.scope["path_remaining"]
        self.roomGroup = f"chat_{self.room}"
        self.accept();

        ats(self.channel_layer.group_add)(
            self.roomGroup, self.channel_name
        )

        self.send(text_data=json.dumps({
            'type':'connected',
            'payload': 'Successful Conection.',
        }))

    def disconnect(self, code):
        ats(self.channel_layer.group_discard)(
            self.roomGroup, self.channel_name
        )

    """ 
    aqui en se recive el mensaje de la conexion de WebSocket 
    entonces se envia a el evento segun el type del mensaje
    """
    def receive(self, text_data):
        data = json.loads(text_data)

        print()

        ats(self.channel_layer.group_send)(
            self.roomGroup, data
        )

    def chatMessage(self, event):
        self.send(text_data=json.dumps(event))