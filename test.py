from main import *


tramp = Tramp()
player = Player()
ai = AI()

print(len(tramp))
print(11 in tramp)

player.update_score()
print(Player())

ai.update_score()
print(AI())

print(tramp[0]+"\n")

for card in tramp:
    print(card)