import os
clear = lambda: os.system('cls')
import msvcrt as m

def textadventure():
    print("Hello! Welcome to Ronstan's text adventure!\nThere are a few rules to fully enjoy this game.\nPress any key to read the next line.\nWhen prompted for a response, refrain from using captital letters.\nThank You and Enjoy!")
    print("")
    username = input("Enter your username to continue: ")
    clear()
    print("Drem yol nok, " + username + ".")
    m.getch()
    print("")
    print("The world you are about to enter is one of dragons and serpents,")
    m.getch()
    print("one of kings and chivalry, ")
    m.getch()
    print("a world different to the secular poison of the 21st century.")
    m.getch()
    print("")
    print("Welcome to Dunlokah")
    print("")
    print("Press any key to continue...")
    m.getch()
    clear()

    #begin story draft 2
    print("It was hazy.")
    m.getch()
    print("")
    print("You could barely make out anything apart from the shadows of tall trees\nwhich had been corrupted by the forest.")
    m.getch()
    print("")
    print("You have no idea why you are here, and shattered memories of a former life\nswirl inside your head.")
    m.getch()
    print("")
    print("Pictures of daisys, girls, cottages, markets, blades, spears:")
    m.getch()
    print("")
    print("They all flash through your mind, although you can't make any sense of it")
    print("")
    print("")
    print("Press any key to continue...")
    m.getch()
    clear()
    print("Suddenly, there is this impending feeling of fear, and the instinct to run")
    m.getch()
    print("")
    print("You don't know what is chasing you- IF something is chasing you.")
    m.getch()
    print("")
    print("The thought is crushed instantaneously in your mind as you focus\non what is ahead.")
    m.getch()
    print("")
    print("You find your way out of all the trees and discover a pathway.")
    m.getch()
    print("")
    print("You have no clue where it leads, but what else are you meant to do?")
    m.getch()
    print("")
    print("You walk along the pathway for what seems like hours, your ragged flesh\ncontinuously making contact with the black, tainted bricks.")
    m.getch()
    clear()
    print("Proceeding down this seemlessy never-ending path is tiresome,")
    m.getch()
    print("")
    print("nothing seems to spike your interest and you feel like giving up.")
    m.getch()
    print("")
    print("You reach a fork in the path which leads left or right")
    m.getch()
    print("")
    print("In front of you lies a sign:")
    m.getch()
    print("")
    print("The sign reads 'Thy left path shall yeild rewards if thou seeks,\nand thy right path shalt be easier, but will bring thou great misfortune")
    m.getch()
    print("")
    userchoice1 = input("Which path will you take? left or right?")
    m.getch()
    clear()
    if(userchoice1 == "left"):
        print("You decide to take the left path.")
        m.getch()
        print("")
        print("The road seems quite similiar to the path you just trod.")
        m.getch()
        print("")
        print("You make your way continuously fowards until a sound breaks the silence")
        m.getch()
        print("")
        print("The sound gets louder and louder as you progress further until\nyou can make out that it is a man's voice")
        m.getch()
        print("")
        print("")
    elif(userchoice1 == "right"):
        print("Come back later for this path")
        m.getch()
    else:
        print("The input you entered was no understood, please enter either left or right.")
        
    
    
    
    
          
    
    
          







textadventure()
    
