import os
import random
import re

os.system('cls' if os.name=='nt' else 'clear')
while (1 < 10):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")
    userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    if not re.match("[SsRrPp]", userChoice):
        print ("Please choose a letter:")
        print ("[R]ock, [S]cissors or [P]aper.")
        print("\n")
        print("Rock, Paper, Scissors - Shoot!")
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print ("I chose: " + opponenetChoice)
    if opponenetChoice == str.upper(userChoice):
        print ("Tie! ")
