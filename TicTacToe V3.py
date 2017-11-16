import random
from time import sleep
import os

def UpdateBoard():
    print " "+Spaces[1]+" | "+Spaces[2]+" | "+Spaces[3]+" "
    print "---+---+---"
    print " "+Spaces[4]+" | "+Spaces[5]+" | "+Spaces[6]+" "        #Basic frame for Each move
    print "---+---+---"
    print " "+Spaces[7]+" | "+Spaces[8]+" | "+Spaces[9]+" "

def ShowNumberBoard():
    print " "+"1"+" | "+"2"+" | "+"3"+" "
    print "---+---+---"
    print " "+"4"+" | "+"5"+" | "+"6"+" "        
    print "---+---+---"
    print " "+"7"+" | "+"8"+" | "+"9"+" "
    
def cls():
    print "\n" * 56


def wait():
    raw_input('Press <ENTER> to continue')

def PlayerOneTurn():
    global UsedSquares
    cls()
    UpdateBoard()
    try:
        P1Input = int(raw_input('Choose a number from one to nine like on a number pad to choose a square: '))
        if P1Input not in UsedSquares and P1Input >= 1 and P1Input <= 9:
            P1Inputted.append(P1Input)
            UsedSquares.append(P1Input)
            Spaces[int(P1Input)] = 'X'
            cls()
            UpdateBoard()
            print "P1:  ", P1Inputted
            print "Com: ", ComInputted
            print "Used:", UsedSquares
    
            wait()
            if CheckWin(P1Inputted,ComInputted) == 'P1':
                print "You win!"
                wait()
                Win(CheckWin(P1Inputted,ComInputted))
            elif CheckWin(P1Inputted,ComInputted) == 'TIE':
                print "It's a tie!"
                wait()
                Win(CheckWin(P1Inputted,ComInputted))
            else:
                ComputerTurn()
        else:
            cls()
            print "Something was wrong with your inputted value"
            print "Please try again"
            wait()
            PlayerOneTurn()        
    except ValueError:
        cls()
        print "There was something wrong with your inputted value"
        wait()
        PlayerOneTurn()
        

def ComputerTurn():
    global ComInputted
    global UsedSquares
    cls()
    ComInput = ComputerSmartChoice()
    ComInputted.append(ComInput)
    try:
        P1Inputted.remove(ComInput)
    except:
        pass
    UsedSquares.append(ComInput)
    Spaces[int(ComInput)] = 'O'

    print "Computer deciding..."
    sleep(2.5)
    cls()
    UpdateBoard()
    print "Computer has made its turn."
    print "ComInput: ", ComInput
    print "P1:  ", P1Inputted
    print "Com: ", ComInputted
    print "Used:", UsedSquares
    wait()
    if CheckWin(P1Inputted,ComInputted) == 'COM':
        print "Computer wins!"
        wait()
        Win(CheckWin(P1Inputted,ComInputted))
    elif CheckWin(P1Inputted,ComInputted) == 'TIE':
        print "It's a tie!"
        wait()
        Win(CheckWin(P1Inputted,ComInputted))
    else:
        PlayerOneTurn()
#Make the comturn syntax mimic playerturn

def ComputerSmartChoice():
    # Variables: ComInputted, psuedoComInputted, psuedoP1Inputted, UsedSquares
    """
    1. Try Win
    2. Try block player
    3. Try Corner
    4. Try Centre
    5. Try Edge
    """
    psuedoComInputted = ComInputted
    psuedoP1Inputted = P1Inputted
    CorrectSquareIndex = 0
    CornerIndices = [1,3,7,9]
    EdgeIndices = [2,4,6,8]
    CentreIndices = [5]
    for meow in range(1,9):
        psuedoComInputted.append(meow)
        if CheckWin(psuedoP1Inputted, psuedoComInputted) == 'COM' and meow not in UsedSquares:
            CorrectSquareIndex = meow
            break
        psuedoComInputted.remove(meow)
    else:
        for meow in range(1,9):
            psuedoP1Inputted.append(meow)
            if CheckWin(psuedoP1Inputted, psuedoComInputted) == 'P1' and meow not in UsedSquares:
                CorrectSquareIndex = meow
                break
            psuedoP1Inputted.remove(meow)
        else:
            random.shuffle(CornerIndices)
            for meow in CornerIndices:
                if meow not in UsedSquares:
                    CorrectSquareIndex = meow
                    break
            else:
                if int(5) not in UsedSquares:
                    CorrectSquareIndex = int(5)
                else:
                    random.shuffle(EdgeIndices)
                    for meow in EdgeIndices:
                        if meow not in UsedSquares:
                            CorrectSquareIndex = meow
                            break
    return CorrectSquareIndex
            
            

def CheckWin(P1List, ComList):
    if sorted(ComList, key=int) in WinList:
        return 'COM'
    elif sorted(P1List, key=int) in WinList:
        return 'P1'
    elif len(UsedSquares) >= 9:
        for meow in WinList:
            if set(meow) < set(ComList):
                return 'COM'                                    #for, else
            elif set(meow) < set(P1List):                       #wowowow
                return 'P1'
        else:
            return 'TIE'
    else:
        for meow in WinList:
            if set(meow) < set(ComList):
                return 'COM'
            elif set(meow) < set(P1List):
                return 'P1'

def Win(Winner):
    cls()
    if Winner == 'P1':
        print "Good Job on Winning!"
    elif Winner == 'COM':
        print "Aww, you didn't win"
    elif Winner == 'TIE':
        print "Wow that was a good game!"
    wait()
    TryAgain = (raw_input("Would you like to try again? (Y/N)")).upper()
    if TryAgain == 'N':
        TryAgain = False
    elif TryAgain == 'Y':                      #Try again code adapted from V1
        TryAgain = True
    else:
        print "Please type something valid"
        wait()
        Win(CheckWin(P1Inputted,ComInputted))

"""
def TryAgain():
    cls()
    Again = (raw_input("Would you like to try again? (Y/N)")).upper()
    if Again == 'N':
        TryAgain = False                  #Was throwing errors I don't know why
    elif Again == 'Y':
        TryAgain = True
    else:
        print "Please input something valid."
        wait()
        TryAgain()
"""
def reset():
    UsedSquares = []
    P1Inputted = []
    ComInputted = []
    P2Inputted = []
    Spaces = {
    1 : ' ',
    2 : ' ',             #DEFAULT MUST BE SPACES 
    3 : ' ',             #Used to update spot on board
    4 : ' ',
    5 : ' ',
    6 : ' ',
    7 : ' ',
    8 : ' ',
    9 : ' ' 
    }

def main():
    reset()
    cls()
    ShowNumberBoard()
    print "This is how the boxes will be numbered on the tic tac toe board."
    wait()
    PlayerOneTurn()

TryAgain = True
if __name__ == "__main__":
    while TryAgain:
        UsedSquares = []
        P1Inputted = []
        ComInputted = []
        P2Inputted = []
        WinList = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        Spaces = {
            1 : ' ',
            2 : ' ',             #DEFAULT MUST BE SPACES 
            3 : ' ',             #Used to update spot on board
            4 : ' ',
            5 : ' ',
            6 : ' ',
            7 : ' ',
            8 : ' ',
            9 : ' ' 
            }
        main()

cls()
print "Thanks for playing!"
wait()
exit()





