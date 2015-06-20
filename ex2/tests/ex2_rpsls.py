#!/usr/bin/env python3
import random
from ex2_rpsls_helper import get_selection

def rpsls_game():
    compRes=0
    userRes=0
    drawRes=0
    while (compRes-userRes)!=2 and (userRes-compRes)!=2:
        userChoice=int(input("    Please enter your selection: "+
              "1 (Rock), 2 (Paper), 3 (Scissors), 4 (Lizard) or 5 (Spock): "))
        if userChoice>5 or userChoice<1:
            print("    Please select one of the available options.\n")
        else:
            print("    Player has selected: %s." %get_selection(userChoice))
            compChoice=random.randint(1, 5)
            print("    Computer has selected: %s." %get_selection(compChoice))

            if userChoice==1:   #Rock
                if compChoice==3 or compChoice==4:
                    print("    The winner for this round is: Player\n")
                    userRes+=1
                elif compChoice==1:
                    print("    This round was drawn\n")
                    drawRes+=1
                else:
                    print("    The winner for this round is: Computer\n")
                    compRes+=1

            elif userChoice==2: #Paper
                if compChoice==1 or compChoice==5:
                    print("    The winner for this round is: Player\n")
                    userRes+=1
                elif compChoice==2:
                    print("    This round was drawn\n")
                    drawRes+=1
                else:
                    print("    The winner for this round is: Computer\n")
                    compRes+=1
  
            elif userChoice==3:    #Scissors
                if compChoice==2 or compChoice==4:
                    print("    The winner for this round is: Player\n")
                    userRes+=1
                elif compChoice==3:
                    print("    This round was drawn\n")
                    drawRes+=1
                else:
                    print("    The winner for this round is: Computer\n")
                    compRes+=1

            elif userChoice==4:   #Lizard
                if compChoice==2 or compChoice==5:
                    print("    The winner for this round is: Player\n")
                    userRes+=1
                elif compChoice==4:
                    print("    This round was drawn\n")
                    drawRes+=1
                else:
                    print("    The winner for this round is: Computer\n")
                    compRes+=1

            else:             #Spock
                if compChoice==1 or compChoice==3:
                    print("    The winner for this round is: Player\n")
                    userRes+=1
                elif compChoice==5:
                    print("    This round was drawn\n")
                    drawRes+=1
                else:  
                    print("    The winner for this round is: Computer\n")
                    compRes+=1
                    
    if compRes>userRes:
        print("The winner for this game is: Computer")
        print("Game score: Player %s, Computer %s, draws %s" % (userRes, compRes, drawRes))
        return -1
    else:
        print("The winner for this game is: Player")
        print("Game score: Player %s, Computer %s, draws %s" % (userRes, compRes, drawRes))
        return 1
        
def rpsls_play():

    setsCount=0
    winCount=0
    gameCount=1
    userSetCount=0
    compSetCount=0
    print("Welcome to the Rock-Scissors-Paper-Lizard-Spock game!")
    setLen=int(input("Select set length: "))
    setEven=setLen
    userQuit=-1
    while userQuit!=1:
        while setLen>0 or compSetCount==userSetCount or +\
              (setEven%2==0 and abs(compSetCount-userSetCount)==1):
            print("Now beginning game %s" %gameCount)
            rpslsRes=rpsls_game()
            if rpslsRes==1:
                userSetCount+=1
            elif rpslsRes==-1:
                compSetCount+=1
            setLen-=1
            gameCount+=1
            print("Set score: Player %s, Computer %s" % (userSetCount, compSetCount))
            if setEven%2==1:
                if ((userSetCount>setEven/2) or (compSetCount>setEven/2)) and compSetCount!=userSetCount :
                    break
            elif setEven%2==0:
                if (compSetCount>setEven/2 or userSetCount>setEven/2) and +\
                   abs(compSetCount-userSetCount)!=1 and compSetCount!=userSetCount:
                    break
        
        if userSetCount>compSetCount:
            print("Congratulations! You have won in %s games." %(gameCount-1))
            winCount+=1
        elif userSetCount<compSetCount:
            print("Too bad! You have lost in %s games." %(gameCount-1))
        setsCount+=1
        print("You have played %s sets, and won %s!\n" %(setsCount, winCount))
        userQuit=int(input("Do you want to: 1 - quit, 2 - reset scores or 3 - continue? "))
        if userQuit==2:
            print("Resetting scores")
            setLen=int(input("Select set length: "))
            setEven=setLen
            setsCount=0
            winCount=0
            gameCount=1
            userSetCount=0
            compSetCount=0
        elif userQuit==3:
            setLen=setEven
            gameCount=1
            userSetCount=0
            compSetCount=0
        elif userQuit==1:
            break
        
    
#Here to help you test your code.
#When debugging, it is helpful to be able to replay with the computer
# repeating the same choices.
if __name__=="__main__": #If we are the main script, and not imported
    from sys import argv
    try:
        random.seed(argv[1]) # as a string is good enough
    except:
        pass

    rpsls_play()
