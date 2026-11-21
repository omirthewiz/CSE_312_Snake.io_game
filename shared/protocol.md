# The contracts (lock these so everyone can build in parallel)

## WebSocket messages
Client -> Server:
    {"type":"input", "dir": 1.57}      # dir = angle in radians toward the mouse

Server -> Client (every tick, ~20/sec):
    {
      "type":"state",
      "snakes":   [ {"id":1,"name":"omir","x":120,"y":80,"body":[]} ],
      "food":     [ {"x":300,"y":220} ],
      "powerups": [ {"x":500,"y":100,"kind":"speed"} ],
      "zone":     {"x":400,"y":300,"r":400}
    }

## JWT (from the auth server)
Signed with RS256. Claims:
    { "username": "omir", "exp": <unix time> }
The app verifies it with the PUBLIC key only (no DB, no call to auth).
