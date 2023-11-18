from art import *
from player_class import player,Enemies
import subprocess
def main():
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
    subprocess.run("cls",shell=True)
    ch_num = text2art("chapitr 1")
    print(ch_num + "\n\tThe first chapter is about a boy named "+str(pl_info.name))
    print("who was born in some year he dont know anything about this world.\n")
    print("one day he get summon to some tower with magical creatures he see one personne and he say")
    print("\twelcome irregulare")
    print(str(pl_info.name)+ " : w-who are you? and where am i?")
    print("unkown: you're in the tower and you're irruglare and if you want more answer you have to go to the top of this tower")
    print("unkown: now you have to face this enimie")
    print("you can choose between two options:\n")
    pl_choise = int(input("1.attack\n2.ran out\n\t please chose one: "))
    if pl_choise == 1:
        print("you start attacking the big bug")
        enemies_instance = Enemies()
        enemy = enemies_instance.eni()
        enemy.health -= pl_info.strength
        if enemy.health <=0:
            print("you killed him")
main()