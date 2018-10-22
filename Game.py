#Brandon Robbins
#10-21-18
#text base adventure game
import random
import time

def displayIntro():
    print("You awake on a planet that you dont reconize and your AI assistant is ..........Unresponsive.""""
    its been who knows how long and you can feel your bones ache when you try and move""")
    #time.sleep(6)
    print()
    print("You wonder weither or not its safe to breathe....... you wont know if you dont try")
    #time.sleep(4)
    print("You take a deep breath in...... ")
    #time.sleep(5)
    print("So begins your adventure into the UNKNOWN!")
    #time.sleep(7)
    print()
    print("You find yourself at fork in a canyon both ways are too curved to see all the way to there destination.......")
    #time.sleep(2)
    print()
    print("Which will you choose?")
    
def choosePath1():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path

def checkPath1(chosenPath1):
    print("You head down the path")
    #time.sleep(3)
    print("you come up on a small station it looks......")
    #time.sleep(2)
    print("Familiar... could this be a good sign?")
   # time.sleep(1)
    print("you begin to feel the hairs on your neck stand up...")
    print()
    #time.sleep(2)
    correctPath1 = random.randint (1, 2)
    if chosenPath1== str(correctPath1):
        print("Must have been nothing..")
        print("How long will your luck last?")
       # time.sleep(2)
        print("there are 2 doors entering the station.")
        print("which on do you choose?")
    if  chosenPath1 != str(correctPath1):
        print("A UNKNOWN alien with a unquienchable thurst for blood mauls you in a instant!")
       # time.sleep(2)
        print("So ends your adventure into the UNKNOWN.")
        global x
        x+=1
   
        
        
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
        print("you find yourself in a dimly lit room with 2 stair cases both going down.")
        print("there is no possible way to see where they lead")
    if chosenPath2 != str(correctPath2):
        print("you take one step and fall into a lazer spike trap and die")
        print("So ends your adventure into the UNKNOWN.")
        global x
        x+=1
        
def choosePath3():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")
        
    return path
def checkPath3(chosenPath3):
    print("You walk down the dimly lit stair case.....")
    print()
    correctPath3=random.randint(1,2)
    if chosenPath3==str(correctPath3):
        print("you go down  stairs without a problem")
        print("how long will your luck last?")
        print("you find yourself at a hallway going left and right")
        print("there no diffrences between the too")
    if chosenPath3 != str(correctPath3):
        print("you go to step down the stair case")
        print("THE STAIRS HAVE BEEN GREESED!")
        print("you slip and fall to your death")
        print("So ends your adventure into the UNKNOWN.")
        global x
        x+=1
        
def choosePath4():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path
def checkPath4(chosenPath4):
    print("you walk down the hallway and start to see a light at the end")
    print()
    correctPath4=random.randint(1,2)
    if chosenPath4==str(correctPath4):
        print("you exit the hallway no problem")
        print("how long will your luck last?")
        print("you find yourself in a cave with a open view to the sky")
        print("you only see 2 ropes on either side of the cave")
    if chosenPath4 !=str(correctPath4):
        print("the light at the end of the tunnel is getting really bright!")
        print(" a huge beam of hard light takes your head clean off!")
        print("so ends your adventure into the UNKNOWN.")
        global x
        x+=1
def choosePath5():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path
def checkPath5(chosenPath5):
    print("you begin to climb and are almost to the top, but you begin to feel the rope slip")
    print()
    correctPath5=random.randint(1,2)
    if chosenPath5==str(correctPath5):
        print("the rope stops slipping and you climb over the side of the cave")
        print("how long will your luck last?")
        print("you find yourself over looking a canyon")
        print(" you spot 2 bridges both identical")
    if chosenPath5 !=str(correctPath5):
        print("the rope continues to slip and you plumit towards the ground")
        print("you get impaled by a stalagmite.")
        print("so ends your adventure into the UNKNOWN.")
        global x
        x+=1

def choosePath6():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path
def checkPath6(chosenPath6):
    print("you begin to cross the bridge")
    print("*CREEEEEEEEK*")
    print("............")
    print()
    correctPath6=random.randint(1,2)
    if chosenPath6==str(correctPath6):
        print("you begin to run towards the otherside of the bridge!")
        print("the bridge colapses and you barely make it")
        print("how long will your luck last?")
        print("you come across a river to wide and fast to swim across")
        print("you spot two identical rafts on the shore")
    if chosenPath6 !=str(correctPath6):
        print("you begin to run but your foot gets caught between the boards")
        print("the bridge collapses and carries you to your painfully death")
        print("so ends your adventure into the UNKNOWN.")
        global x
        x+=1



        #Start Here
        
        
    
    


x=0
 
    

def game_over():
    global x
    global playAgain
   
    if x>0:
        playAgain="YOU DIED"
        

playAgain="yes"
while playAgain=="yes" or playAgain=="y":
    displayIntro()
    choice1 = choosePath1()
    checkPath1(choice1)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice2 =choosePath2()
    checkPath2(choice2)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice3=choosePath3()
    checkPath3(choice3)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice4=choosePath4()
    checkPath4(choice4)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice5=choosePath5()
    checkPath5(choice5)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice6=choosePath6()
    checkPath6(choice6)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
    print()
    print()
    print()


