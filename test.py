from main import *


tramp = Tramp()
player = Player()
ai = AI()

print(tramp.__len__())
print(11 in tramp)

player.update_score()
print(Player())

ai.update_score()
print(AI())

print(f"{tramp[0]}\n")

deck = Tramp()
print(deck)
print(deck.__reversed__())