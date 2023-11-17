from art import *
class player:
    def __init__(self, name,gender):
        self.name = name
        self.xp = 0
        self.gender = gender
        
    def moving(self):
        print("moving")
title = text2art("QUEST QUASAR")
print(title)
print("hello, player to QUEST QUASAR where you'll have to face danger or be the danger gain more power to face your enimes")
pl_name = input("first what's your name: ")
pl_gender = int(input("what's your gender? (1 for male and 2 for female): "))
if pl_gender == 1:
    pl_gender = "male"
elif pl_gender == 2:
    pl_gender = "female"
else:
    print("wrong answer! try again.")
pl_info = player(pl_name,pl_gender)
print("\n\tWelcome to the world of Quest Quasar!\n")

