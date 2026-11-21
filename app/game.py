# ===== GAME SERVER - OWNER: Person 3 =====
# Holds all game state and runs the loop. Fill in the TODOs.
import asyncio, json, math, random

players = {}
nextid = 1
food = []                              # TODO: spawn food
powerups = []                          # TODO: spawn power-ups (speed, ghost, magnet...)
zone = {"x": 400, "y": 300, "r": 400}  # TODO: shrink r over time, kill snakes outside it

def addplayer(sock, name=None):
    global nextid
    pid = nextid
    nextid += 1
    players[pid] = {"sock": sock, "name": name or f"p{pid}",
                    "x": random.random()*800, "y": random.random()*600, "dir": 0, "body": []}
    return pid

def removeplayer(pid):
    players.pop(pid, None)

def handleinput(pid, msg):
    if msg.get("type") == "input" and pid in players:
        players[pid]["dir"] = msg.get("dir", 0)

async def loop():
    while True:
        tick()
        await broadcast()
        await asyncio.sleep(1/20)      # 20 ticks per second

def tick():
    # TODO Person 3: move each snake by its dir, grow its body, check collisions
    #   (snake vs snake, snake vs food, snake vs power-up, snake vs zone edge)
    for p in players.values():
        p["x"] += math.cos(p["dir"]) * 3
        p["y"] += math.sin(p["dir"]) * 3

async def broadcast():
    state = json.dumps({"type": "state", "snakes": snapshot(),
                        "food": food, "powerups": powerups, "zone": zone})
    for p in list(players.values()):
        try:
            await p["sock"].send_text(state)
        except Exception:
            pass

def snapshot():
    return [{"id": pid, "name": p["name"], "x": p["x"], "y": p["y"], "body": p["body"]}
            for pid, p in players.items()]
