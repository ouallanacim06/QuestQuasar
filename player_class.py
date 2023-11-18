import random
for i in range(1):
    if i == 0:
        ran_nu = random.randint(1,50)
        while i == 0:
            i+=1
            rand_num = ran_nu
        print("Random number is",ran_nu,rand_num)
class player:
    def __init__(self, name,gender):
        self.name = name
        self.xp = 0
        self.gender = gender
        self.strength = ran_nu
        self.intelligence = 1
        self.agility = 1
        self.health = 50
        self.max_health = 50

    
class player_action:
    def move(self, action):
        self.move = action
        self.battle = action
class Enemies:
    def eni(self):
        enemy = Enemies()
        enemy.health = random.randint(1,5)
        enemy.attack = random.randint(1,2)
        enemy.name = "enemy"
        return enemy