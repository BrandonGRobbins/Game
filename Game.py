#Brandon Robbins
#10-21-18
#text base adventure game
import random
import time

def displayIntro():
    print("You awake on a planet that you dont reconize and your AI assistant is ..........Unresponsive.""""
    its been who knows how long and you can feel your bones ache when you try and move""")
    time.sleep(6)
    print()
    print("You wonder weither or not its safe to breathe....... you wont know if you dont try")
    time.sleep(4)
    print("You take a deep breath in...... ")
    time.sleep(5)
    print("So begins your adventure into the UNKNOWN!")
    time.sleep(7)
    print()
    print("You find yourself at fork in a canyon both ways are too curved to see all the way to there destination.......")
    time.sleep(2)
    print()
    print("Which will you choose?")
    
def choosePath1():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path

def checkPath1(chosenPath1):
    print("You head down the path")
    time.sleep(3)
    print("you come up on a small station it looks......")
    time.sleep(2)
    print("Familiar... could this be a good sign?")
    time.sleep(1)
    print("you begin to feel the hairs on your neck stand up...")
    print()
    time.sleep(2)
    correctPath1 = random.randint (1, 2)
    if chosenPath1== str(correctPath1):
        print("Must have been nothing..")
        print("How long will your luck last?")
        time.sleep(2)
        print("there are 2 doors entering the station.")
        print("which on do you choose?")
    if  chosenPath1 != str(correctPath1):
        print("A UNKNOWN alien with a unquienchable thurst for blood mauls you in a instant!")
        time.sleep(2)
        print("So ends your adventure into the UNKNOWN.")
        
def choosePath2():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")
        
    return path
def checkPath2(chosenPath2):
    print("you approch the the chosen door")
    print("you turn the door knob and go to step inside...")
    print()
    correctPath2=random.randint(1, 2)
    if chosenPath2==str(correctPath2):
        print("you walk into the station without any problems")
        print("How long will you luck last?")
    if chosenPath2 != str(correctPath2):
        print("you take one step and fall into a lazer spike trap and die")
        print("So ends your adventure into the UNKNOWN.")
def choosePath3():
     path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")
        
    return path
def checkPath3(chosenPath3):
    print("you find yourself in a dimly lit room with 2 stair cases both going down.")
    


#start here!!


  

    
playAgain="yes"
while playAgain=="yes" or playAgain=="y":
    displayIntro()
    choice1 = choosePath1()
    checkPath1(choice1)
    choice2 =choosePath2()
    checkPath2(choice2)
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
    print()
    print()
    print()
