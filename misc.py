import os
from player import Player
import random
import item
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#This is all the ascii art that would have been too much if it was ALL in the main
#the two choice inputs decide if I want a blank scrren/ input after displaying my beautiful art
def Reed(clearchoice,inputchoice):
    if clearchoice==True:
        clear()
    print("    ___            _ ")
    print("   | _ \___ ___ __| |")
    print("   |   / -_) -_) _` |")
    print("   |_|_\___\___\__,_|")
    print()
    if inputchoice==True:
        input("Press enter to continue...")

def Chem(clearchoice,inputchoice):

    if clearchoice==True:
        clear()
    print("                                                       .:")
    print("                                                      / )")
    print("                                                     ( (")
    print("                                                      \ )")
    print("      o                                             ._(/_.")
    print("       o                                            |___%|")
    print("     ___              ___  ___  ___  ___             | %|")
    print("     | |        ._____|_|__|_|__|_|__|_|_____.       | %|")
    print("     | |        |__________________________|%|       | %|")
    print("     |o|          | | |%|  | |  | |  |~| | |        .|_%|.")
    print("    .' '.         | | |%|  | |  |~|  |#| | |        | ()%|")
    print("   /  o  \        | | :%:  :~:  : :  :#: | |     .__|___%|__.")
    print("  :____o__:     ._|_|_."    "    "    "._|_|_.   |      ___%|_")
    print("  '._____.'     |___|%|                |___|%|   |_____(____  )")
    print("                                                           ( (")
    print("                                                            \ '._____.-")
    print("                                                             '.___grp_.- "     )
    if inputchoice==True:
        input("Press enter to continue...")
def Scholz(clearchoice,inputchoice):

    if clearchoice==True:
        clear()
    print(" _______________________________")
    print("|.'''|==;              ;===|'.'.|")
    print("|.'''|::|',          ,|:::|.'..'|")
    print("|.'''|--|'.| _____ ,|.|---|.'.'.|")
    print("|.'''|::|'.||TTTTT|'|.|:::|.'.'.|")
    print("|,'''|--|',||TTTTT|'|,|---|,',',|")
    print("|.'''|::|'.||TTTTT|'|.|:::|.'.'.|")
    print("|.'' |--|',' /X\  ,|--|'.'|''.'.|")
    print("|.'' |==:'  /XXX\  :==|.'.'|.'.'|")
    print("|.'' |XXXXXXXXXXXXXXXX|.''|''.'.|")
    print("|.'' |    /XXXXXXX\  ','.'|.'.'.|")
    print("|.''''   /XXXXXXXXX\   '''|'.'.'|")
    print("|.''    /XXXXXXXXXXX\    '|'.'.'|")
    print("|.''   /XXXXXXXXXXXXX\     ','.'|")
    print("|;____/XXXXXXXXXXXXXXX\_______;;|")
    if inputchoice==True:
        input("Press enter to continue...")

def craft(player):
    t = input('Do you want to try crafting? Yes or No ')
    if t.lower() == "yes":
        clear()
        #Gotta have rotten flesh!
        if player.playerItem('rotten flesh'):

            input("You tinker quite a bit with some rotten flesh...")
            print()

            r=random.random()
            if r>.6:
                #Currently set at a 40% success rate ( I think I lied earlier haha )
                print("And create the cure!")
                print("You hastily drink up the vial of mysterious liquid")
                print("and feel anti-zombie powers seep into your skin")

                player.wonGame=True
                #You don't need to be alive if you've already won!
                player.alive=False
            else:
                target = player.playerItem('rotten flesh')
                print("You make a silly mistake when crafting and ruin the rotten flesh.\nMaybe next time you'll get it right")
                input("Press enter to continue...")
                print()
                player.items.remove(target)
                player.carrying-=.5
        else:
            print("\nBroken test tubes are scattered about...\n And you need something to tinker with...\nYeah, maybe next time.")
            input("Press enter to continue...")
    else:
        print("You move on your way, carefully avoiding shards of glass.")
        input("Press enter to continue...")

def Nog(clearchoice,inputchoice):
    #It's a squid :D
    if clearchoice==True:
        clear()
    print ("      ________________")
    print("    //       ^        \\")
    print("    ||     /   \      ||    ")
    print("    ||     \   /      ||     ")
    print("    ||     |   |      ||  ")
    print ("    ||     |   |      ||  ")
    print ("    ||     | 0 |      || ")
    print("    ||    // ||\\\\     || ")
    print("    ||   (( // ||     ||  ")
    print("    ||    \\\\))  \\\\    || ")
    print("    ||    //||   ))   ||     ")
    print("    ||    ( ))  //    || ")
    print("    ||    //   ((     ||   ")
    print("    \\\\________________//")
    if inputchoice==True:
        input("Press enter to continue...")

def CSO(clearchoice,inputchoice):

    if clearchoice==True:
        clear()
    print("  _________________________")
    print(" /////////////|\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print("'.-------------------------.'")
    print(" |                         |")
    print(" | [] [] [] [] [] [] [] [] |")
    print(" |                         |")
    print("_.-.        28 West        |")
    print(">   )] [] []||_|_||[] [] []|,'`\\")
    print("`.,'________||_|_||________|\  <")
    print("||  /  _<> _     _    (_)<>\ ||")
    print("'' /<>(_),:/     \:. <>'  <>\||")
    if inputchoice==True:
        input("Press enter to continue...")
def Library(clearchoice,inputchoice):

    if clearchoice==True:
        clear()
    print(" ________________________________________________________")
    print("||------------------------------------------------------||")
    print("||.--.    .-._                        .---.             ||")
    print("|||==|____| |H|___            .---.___|'Z'|_____.--.___ ||")
    print("|||  |====| | |xxx|_          |+++|=-=|_O_|-=+=-|==|---|||")
    print("|||==|    | | | D | \         |   |   |_M_| FIND|  | ^ |||")
    print("|||  |    | | | I |\ \   .--. |   |=-=|_B_|-THE-|  | ^ |||")
    print("|||  |    | | | E |_\ \_( oo )|   |   | I | CURE|  | ^ |||")
    print("|||==|====| |H|xxx|  \ \ |''| |+++|=-=|'E'|-=+=-|==|---|||")
    print("||`--^----'-^-^---'   `-' ""  '---^---^---^-----^--^---^||")
    print("||------------------------------------------------------||")
    print(" ________________________________________________________")
    if inputchoice==True:
        input("Press enter to continue...")
def Commons(clearchoice,inputchoice):

    if clearchoice==True:
        clear()
    print()
    print("                       ,II,     ")
    print("                      ,I;;I, ")
    print("          ,           I~@@~I           ,   ")
    print("        , I ,         ;\;;/;         , I ,         ")
    print("      __I~@~I__       `;;;;`       __I~@~I__        ")
    print("!____/  ;\_/;  \____!___)(___!____/  ;\_/;  \____!")
    print("|__ /___________\ __|  (__)  |__ /___________\ __|")
    print("[__]     | |     [__]        [__]     | |     [__] ")
    print(" )(     _) (_     )(          )(     _) (_     )(   ")


    if inputchoice==True:
        input("Press enter to continue...")




def Rubble(clearchoice,inputchoice):
    #Most rooms are this
    if clearchoice==True:
        clear()
    print("              +         .      .    | .      `|||.:      .||    .      .    `")
    print("          '                           `|.   .  `:|||   + ||'     `")
    print("  __    +      *                         `'       `'|.    `:")
    print("'  `---\"\"\"----....____,..^---`^``----.,.___          `.    `.  .    ____,.,-")
    print("    ___,--'\"\"`---\"'   ^  ^ ^        ^       \"\"\"'---,..___ __,..---\"\"'")
    print("--\"'                           ^                         ``--..,__ ________")
    if inputchoice==True:
        input("Press enter to continue...")
