from  dataclasses import dataclass
from fastapi import WebSocket
from typing import List
# ======================== Exemplo: https://fastapi.tiangolo.com/advanced/websockets/

@dataclass(repr=False, eq=False, match_args=False, slots=True)
class UserChat():
    name:str
    id_user:int
    websocket_connection:WebSocket


@dataclass(repr=False, eq=False, match_args=False, slots=True)
class ConnectionManager:
    active_connections: List[UserChat]

    async def connect(self, user_chat: UserChat):
        await user_chat.websocket_connection.accept()
        self.active_connections.append(user_chat)

    def disconnect(self, user_chat: UserChat):
        self.active_connections.remove(user_chat)

    async def send_personal_message(self, message: str, user_chat: UserChat):
        await user_chat.websocket_connection.send_text(message)

    async def broadcast(self, message: str):
        for user_chat in self.active_connections:
            await user_chat.websocket_connection.send_json(message)
    
    async def sendAllUsersConnectedToUser(self, current_user_chat: UserChat):
        for user_chat in self.active_connections:
            if user_chat.id_user != current_user_chat.id_user and user_chat.name != 'defalt':
                jsonUserConnect ={
                        "id_user": user_chat.id_user,
                        "user_name": user_chat.name,
                        "action": "connect"
                    }
                await current_user_chat.websocket_connection.send_json(jsonUserConnect)

manager = ConnectionManager([])