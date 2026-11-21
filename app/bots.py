# ===== AI BOTS (Objective 4) - OWNER: You (Person 4) =====
# A bot is a fake player. Each tick it looks at the game state, picks a dir,
# then calls game.handleinput(botid, {"type":"input","dir":dir}) - just like a human.
#
# Plan for each bot, each tick:
#   1. find the nearest food -> steer toward it
#   2. if another snake's body is close -> steer away
#   3. if outside / near the edge of the shrinking zone -> steer back in
#   4. if a power-up is close -> grab it
#
# import game
# def spawnbot():
#     ...  # add a fake player, run a loop that sets its dir each tick
