# ===== JWT VERIFY (used by the game) - OWNER: Person 2 writes, app uses =====
# Verify the token with the PUBLIC key only. No DB, no call to the auth server.
#
# import jwt
# pub = open("/pub/public.pem").read()
# def verify(token):
#     try:
#         return jwt.decode(token, pub, algorithms=["RS256"])  # rejects bad sig / wrong alg / expired
#     except Exception:
#         return None
