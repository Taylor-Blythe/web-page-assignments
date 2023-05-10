"""
Intro dialog: the hero makes to the castle blah blah blah
while(boss not beaten)
Castle Maze: left, right, center mase esque (keep it simple)

--------------|-----------|---------Big bad
if/else section: If left dead end else if right deadend else fight skely

Fight a skeley
Fight or Run
IF fight enter fight while loop
Choices of attack: Sword, Magic, Hands

Crit if health < 50% and randint > 50: crit success

Rest maze

Fight big bad
end while

end credits
"""


import time
from datetime import datetime as dt
from random import randint 
intro_dialog = ["this is the world of Sftg sgyhsrhedrth", "you are the hero!", "summoned to slay the demon king!", "go do it"]
choice_dialog = ["there is a long hallway in front of you", "a door to the left", "a door to the right", "which way"]



#Funciton for printing dialog like a video game
def printDialog(dialog, speed=1/30):
    for line in dialog:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(speed)
        print("")

#Intro dialog
printDialog(intro_dialog)

input("Enter to continue")


#Maze phase
printDialog(choice_dialog)
skelly = True
while(skelly):
    
    userchoice = input("Left, Right, Forward: ")
    if(userchoice.lower() == "left" or userchoice.lower() == "l"):
        printDialog(["That's a dead end"])
    elif(userchoice.lower() == "right" or userchoice.lower() == "r"):
        printDialog(["That's a dead end"])
    elif(userchoice.lower() == "forward" or userchoice.lower() == "f"):
        printDialog(["You have encounterd a skelly"])
        skelly = False
    
    else:
        printDialog(["That's not an option"])

printDialog(["FIGHT THE SKELETON!!!!!"])
skellyHP = 100
while skellyHP > 0:
    userchoice = input("run, fight: ")
    if(userchoice.lower() == "run" or userchoice.lower() == "r"):
        printDialog(["you can't run"])
    elif(userchoice.lower() =="fight" or userchoice.lower() =="f"):
        while(skellyHP > 0):
            crit = 1
            userchoice = input("sword, fireball, or HANDS: ")
            if(userchoice.lower() == "sword" or userchoice.lower() == "s"):
                if randint(0,100) > 50:
                    crit = 2
                skellyHP=skellyHP-1 * crit
                printDialog([f"the skelly has {skellyHP}HP"])
            elif(userchoice == "HANDS" or userchoice.lower() == "h"):
                if randint(0,100) > 10:
                    crit = 2
                skellyHP=skellyHP-999999*crit
                printDialog([f"the skelly has caught these hands and now has {skellyHP}HP"])
            elif(userchoice.lower() == "fireball" or userchoice.lower() == "f"):
                skellyHP=skellyHP-30
                printDialog([f"the skelly has {skellyHP}HP"])
            else:
                printDialog(["That's not an option"])
printDialog(["you beat da skelly!"])
printDialog(["The demon king appears!"])
printDialog(["FIGHT THE DEMON KING!!!!!"])

demonkingHP = 100
while demonkingHP > 0:
    userchoice = input("run, fight: ")
    if(userchoice.lower() == "run" or userchoice.lower() == "r"):
        printDialog(["you can't run"])
    elif(userchoice.lower() =="fight" or userchoice.lower() =="f"):
        while(demonkingHP > 0):
            crit = 1
            userchoice = input("sword, fireball, or HANDS: ")
            if(userchoice.lower() == "sword" or userchoice.lower() == "s"):
                if randint(0,100) > 50:
                    crit = 2
                demonkingHP=demonkingHP-1
                printDialog([f"the demon king has {demonkingHP}HP"])
            elif(userchoice == "HANDS" or userchoice.lower() == "h"):
                if randint(0,100) > 10:
                    crit = 2
                demonkingHP=demonkingHP-999999
                printDialog([f"the demon king has caught these hands and now has {demonkingHP}HP"])
            elif(userchoice.lower() == "fireball" or userchoice.lower() == "f"):
                demonkingHP=demonkingHP-30
                printDialog([f"the demon king has {demonkingHP}HP"])
            else:
                printDialog(["That's not an option"])
printDialog(["you beat da demonking!"])
printDialog([f"you beat demonking at {dt.now()}......gj"])