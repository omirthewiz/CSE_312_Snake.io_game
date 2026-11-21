# ===== AUTH SERVER (Objective 2) - OWNER: Person 2 =====
import os
from fastapi import FastAPI, Request
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

app = FastAPI()

# Make an RS256 key pair ONCE and keep it. Private key stays here (/keys);
# the public key is copied to the shared /pub volume so the app can verify tokens.
if not os.path.exists("/keys/private.pem"):
    os.makedirs("/keys", exist_ok=True)
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    priv = key.private_bytes(serialization.Encoding.PEM,
                             serialization.PrivateFormat.PKCS8,
                             serialization.NoEncryption())
    pub = key.public_key().public_bytes(serialization.Encoding.PEM,
                                         serialization.PublicFormat.SubjectPublicKeyInfo)
    open("/keys/private.pem", "wb").write(priv)
    open("/keys/public.pem", "wb").write(pub)

os.makedirs("/pub", exist_ok=True)
open("/pub/public.pem", "wb").write(open("/keys/public.pem", "rb").read())

# TODO Person 2:
#   /register -> hash password (bcrypt), save user in Postgres
#   /login    -> check password, sign a JWT (RS256, include exp), set it as a cookie
#   /logout   -> clear the cookie
@app.post("/register")
async def register(req: Request):
    return "TODO: register"

@app.post("/login")
async def login(req: Request):
    return "TODO: login"

@app.get("/logout")
async def logout():
    return "TODO: logout"
