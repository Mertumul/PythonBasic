print(" Player Registaration Program")

name = input("Player's Name:")
surname = input("Player's Surname:")
age = int(input("Player's Age:"))
team = input("Player's Team")

information = [name, surname, age, team]

print("Information being saved ...")

print("Player Name:{}\nPlayer Surname:{}\nPlayer Age:{}\nPlayer Team:{}".format(
    name, surname, age, team))
