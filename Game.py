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
        print("the bridge collapses and carries you to your painful death")
        print("so ends your adventure into the UNKNOWN.")
        global x
        x+=1

def choosePath7():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path
def checkPath7(chosenPath7):
    print("you hop into the raft and begin to paddle accross the river")
    print("you see the see a dorsal fin pop up out of the water")
    print()
    correctPath7=random.randint(1,2)
    if chosenPath7==str(correctPath7):
        print("the fin dips back into the water and you continue paddling")
        print("how long will your luck last.")
        print("you hop out of the boat and are met with 2 paths")
    if chosenPath7 !=str(correctPath7):
        print("the fin gets closer and closer to your boat.")
        print(" you see teeth the size of dinner plates surround your raft!")
        print("CHOMP")
        print("So ends your adventure into the UNKNOWN.")
        global x
        x+=1
def choosePath8():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path
def checkPath8(chosenPath8):
    print("you head down the path")
    print("you find yourself under a tree")
    print("you also spot a strange bird over head")
    print()
    correctPath8=random.randint(1,2)
    if chosenPath8==str(correctPath8):
        print("the bird flies away leaving you to go about your buisness")
        print("how long will your luck last?")
        print("you spot 2 rabbit holes at the base of the tree.")
    if chosenPath8!=str(correctPath8):
        print("you see the bird get closer and closer")
        print("the bird picks you up and takes you to its nest where its babies eat you")
        print("so ends your adventure into the UNKNOWN.")
        global x
        x+=1
def choosePath9():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path
def checkPath9(chosenPath9):
    print("you head down the rabbit hole.")
    print("you find yourself in a dark cave")
    print("you also hear a light hum")
    print()
    correctPath9=random.randint(1,2)
    if chosenPath9==str(correctPath9):
        print("the light hum begins to fade away.")
        print("how long will your luck last?")
        print("you spot 2 torches on a wall")
    if chosenPath9!=str(correctPath9):
        print("the humming gets louder and louder.")
        print("you soon are completely surrounded by bees")
        print("you get stung so much you inflate like a balloon and POP!")
        print("so ends your adventure into the UNKNOWN")
        global x
        x+=1
def choosePath10():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path    
def checkPath10(chosenPath10):
    print("you grab the touch off the wall ")
    print("you begin to feel the tourch getting hot")
    print()
    correctPath10=random.randint(1,2)
    if chosentPath10==str(correctPath10):
        print("its a torch of course its hot.")
        print("how long will your luck last?")
        print("the touch gets brighter and reveils 2 corrodors")
    if chosenPath10!=str(correctPath10):
        print("so the touch gets even hotter")
        print("soon you are completely ingulfed in flames.")
        print("so ends your adventure into the UNKNOWN.")
        global x
        x+=1
        
def choosePath11():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path
def checkPath11(chosenPath11):
    print("you walk down the corrodor")
    print("you hear a gun go off behind you")
    print()
    correctPath11=random.randint(1,2)
    if chosenPath11==str(correctPath11):
        print("the bullet wizzez past your face!")
        print("how long will your luck last?")
        print("you find yourself over looking a lake")
        print("you also spot 2 diving suits")
    if chosenPath11!=str(correctPath11):
        print("the bullet goes right through the back of your skull and you fall face first into the dirt.")
        print("so ends your adventure into the UNKNOWN.")
        global x
        x+=1
def choosePath12():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path
def checkPath12(chosenPath12):
    print("you put on the diving suit")
    print("you cant breath!")
    print()
    correctPath12=random.randint(1,2)
    if chosenPath12==str(correctPath12):
        print("turns out you were standing on the oxygen tube.")
        print("how long will your luck last?")
        print("you dive into the water and find 2 plugs at the bottom")
        print()
    if chosenPath12!=str(correctPath12):
        print(" you try to take the helmit off in your panic")
        print ("but alas it is stuck and you suffocate to death")
        print(" so ends the adventure into the UNKNOWN.")
        global x
        x+=1
def choosePath13():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path
def checkPath13(chosenPath13):
    print("you remove the plug.")
    print()
    correctPath13=random.randint(1,2)
    if chosenPath13==str(correctPath13):
        print("the water from the lake begins to drain.")
        print("you find yourself in a underground bunker")
        print("how long will your luck last?")
        print("you also see two doors both 10 inches of unbreakable steel.")
        print()
    if chosenPath13!=str(correctPath13):
        print("the second you remove the plug thousands of parana escape.")
        print("they chew the meat of your bones until your a dead spooky skeleton.")
        print("so ends your adventure into the UNKNOWN.")
        global x
        x+=1
def choosePath14():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")

    return path
def checkPath14(chosenPath14):
    print("you open the door.")
    print("the door makes a deafining SKREEEEECH.")
    print()
    correctPath14=random.randint(1,2)
    if chosenPath14==str(correctPath14):
        print("your ears a ringing a bit but youll be fine.")
        print("how long will your luck last.")
        print("you walk through the door and see a wall with 2 levers.")
        print()
    if chosenPath14!=str(correctPath14):
        print("the door screeches so loud that your head explodes.")
        print("so ends your adventure into the UNKNOWN.")
        global x
        x+=1
def choosePath15():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")    

    return path
def checkPath15(chosenPath15):
    print(" you pull the leaver")
    print("you feel the floor shift underneath you")
    print()
    correctPath15=random.randint(1,2)
    if chosenPath15==str(correctPath15):
        print("the floor opens up!")
        print("and you begin to slide down a slide")
        print("how long will your luck last?")
        print("you find yourself in a room")
        print("the room has 2 glowing portals")
    if chosenPath15!=str(correctPath15):
        print("the floor opens up!")
        print("and you fall down and endless pit and you starve to death")
        print("so ends your adventure into the UNKNOWN")
        global x
        x+=1

def choosePath16():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")    

    return path
def checkPath16(chosenPath16):
    print("you walk through the portal")
    print("you start to feel funny")
    print()
    correctPath16=random.randint(1,2)
    if chosenPath16==str(correctPath16):
        print("you go through the portal and throw up once you exit")
        print("not enough to die")
        print("how long will your luck last?")
        print("you find yourself in the same space station as before.")
        print("with the same stairs.")
    if chosenPath16!=str(correctPath16):
        print(" you dont know how long you've in the portal")
        print("long enough to die thats for sure.")
        print("so ends your adventure into the UNKNOWN.")
        global x
        x+=1
def choosePath17():
    path=""
    while path !=  "1" and path != "2":
        path= input("Which path will you choose?  (1 or 2): ")    

    return path
def checkPath17(chosenPath17):
    print("you walk down the stairs")
    print(" they seem to be going on forever")
    print()
    correctPath17=random.randint(1,2)'
    if chosenPath17==str(correctPath17):
        print()


#start here










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
    choice7=choosePath7()
    checkPath7(choice7)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice8=choosePath8()
    checkPath8(choice8)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice9=choosePath9()
    checkPath9(choice9)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice10=choosePath10()
    checkPath10(choice10)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice11=choosePath11()
    checkPath11(choice11)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice12=choosePath12()
    checkPath12(choice12)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice13=choosePath13()
    checkPath13(choice13)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice14=choosePath14()
    checkPath14(choice14)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice15=choosePath15()
    checkPath15(choice15)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    choice16=choosePath16()
    checkPath16(choice16)
    game_over()
    print(playAgain)
    if playAgain=="YOU DIED":
        break
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
    print()
    print()
    print()


