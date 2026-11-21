# Wires FastAPI + websockets together. Shared base - don't rewrite, just plug in.
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
import game

app = FastAPI()

@app.websocket("/ws")
async def ws(sock: WebSocket):
    await sock.accept()
    # TODO (Person 2's JWT verify goes here): reject the connection if the token is bad.
    pid = game.addplayer(sock)
    try:
        while True:
            msg = await sock.receive_json()
            game.handleinput(pid, msg)
    except WebSocketDisconnect:
        game.removeplayer(pid)

@app.on_event("startup")
async def startup():
    asyncio.create_task(game.loop())

# serve the client (keep this LAST so it doesn't shadow /ws)
app.mount("/", StaticFiles(directory="public", html=True), name="public")
