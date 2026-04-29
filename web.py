# from fastapi import FastAPI, WebSocket, WebSocketDisconnect

# app = FastAPI(title="WEBSOCKET IMPLEMENTATION")


# class ConnectionManager:

#     def __init__(self):
#         self.active_connections = []

#     async def connect(self, websocket):
#         await websocket.accept()
#         self.active_connections.append(websocket)

#     def disconnect(self, websocket):
#         self.active_connections.remove(websocket)

#     async def broadcast(self, message):
#         for connection in self.active_connections:
#             await connection.send_text(message)


# manager = ConnectionManager()


# @app.get("/")
# def home():
#     return {"message": "First time websockets"}


# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     print("websocket route hit")
#     await manager.connect(websocket)

#     try:
#         while True:
#             data = await websocket.receive_text()

#             await manager.broadcast(f"User says: {data}")

#     except WebSocketDisconnect:

#         manager.disconnect(websocket)

#         print("Client disconnected")


from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

app = FastAPI(title="WEBSOCKET IMPLEMENTATION")


class ConnectionManager:

    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


html = """
<!DOCTYPE html>
<html>
<head>
<title>Mini Chat</title>

<style>
body{
font-family:Arial;
max-width:700px;
margin:30px auto;
}

#messages{
border:1px solid #ccc;
height:300px;
overflow-y:auto;
padding:15px;
margin-bottom:15px;
}

input{
width:70%;
padding:10px;
}

button{
padding:10px 20px;
}
</style>

</head>
<body>

<h2>FastAPI WebSocket Chat</h2>

<div id="messages"></div>

<input id="messageText"
placeholder="Type message"/>

<button onclick="sendMessage()">
Send
</button>

<script>

let ws = new WebSocket(
"ws://127.0.0.1:8000/ws"
);


ws.onopen = function(){
console.log("Connected");
};


ws.onmessage = function(event){

let msgBox =
document.getElementById(
"messages"
);

let p =
document.createElement("p");

p.textContent = event.data;

msgBox.appendChild(p);

msgBox.scrollTop=
msgBox.scrollHeight;

};


function sendMessage(){

let input=
document.getElementById(
"messageText"
);

if(input.value.trim()!=""){

ws.send(input.value);

input.value="";

}

}

</script>

</body>
</html>
"""


@app.get("/")
async def home():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("websocket route hit")

    await manager.connect(websocket)

    try:
        while True:

            data = await websocket.receive_text()

            await manager.broadcast(f"User says: {data}")

    except WebSocketDisconnect:

        manager.disconnect(websocket)

        print("Client disconnected")
