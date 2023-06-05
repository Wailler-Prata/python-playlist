from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect
from fastapi.templating import Jinja2Templates
from portifolio_code.websocket import manager, UserChat


app_routes = APIRouter()
templates = Jinja2Templates(directory='templates')

@app_routes.get("/")
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app_routes.websocket("/ws/{client_id}/{user_name}")
async def websocket_endpoint(websocket: WebSocket, client_id: int, user_name:str = "defalt"):
    user_chat = UserChat(name=user_name, id_user=client_id, websocket_connection=websocket)
    await manager.connect(user_chat)   
    jsonUserConnect ={
        "id_user": user_chat.id_user,
        "user_name": user_chat.name,
        "action": "connect"
    }
    await manager.sendAllUsersConnectedToUser(user_chat) 
    await manager.broadcast(jsonUserConnect)
    
    try:        
        while True:
            data = await websocket.receive_json()
            jsonResponse = {
                "id_user" : user_chat.id_user,
                "user_name": user_chat.name,
                "message": data['message']
            }
            await manager.broadcast(jsonResponse)

    except WebSocketDisconnect:
        manager.disconnect(user_chat)
        jsonUserDisconnect ={
                    "id_user": user_chat.id_user,
                    "user_name": user_chat.name,
                    "action": "disconnect"
                }
        await manager.broadcast(jsonUserDisconnect)