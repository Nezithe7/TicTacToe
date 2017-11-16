import random
from time import sleep
import os

def UpdateBoard():
    print " "+Spaces[1]+" | "+Spaces[2]+" | "+Spaces[3]+" "
    print "---+---+---"
    print " "+Spaces[4]+" | "+Spaces[5]+" | "+Spaces[6]+" "        #Basic frame for Each move
    print "---+---+---"
    print " "+Spaces[7]+" | "+Spaces[8]+" | "+Spaces[9]+" "

def cls():
    print "\n" * 56


def wait():
    raw_input('Press <ENTER> to continue')

def PlayerOneTurn():
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
            wait()
            if CheckWin() == 'P1':
                print "You win!"
                wait()
                Win(CheckWin())
            elif CheckWin() == 'TIE':
                print "It's a tie!"
                wait()
                Win(CheckWin())
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
    cls()
    ComInput = random.randint(1,9)
    ComInputted.append(ComInput)
    UsedSquares.append(ComInput)
    Spaces[int(ComInput)] = 'O'
    print "Computer deciding..."
    sleep(2.5)
    cls()
    UpdateBoard()
    print "Computer has made its turn."
    wait()
    if CheckWin() == 'COM':
        print "Computer wins!"
        wait()
        Win(CheckWin())
    elif CheckWin() == 'TIE':
        print "it's a tie!"
        wait()
        Win(CheckWin)
    else:
        PlayerOneTurn()

def ComputerSmartChoice():
    # Variables: ComInputted
    pass

def CheckWin():
    if sorted(ComInputted, key=int) in WinList:
        return 'COM'
    elif sorted(P1Inputted, key=int) in WinList:
        return 'P1'
    elif len(UsedSquares) >= 9:
        for meow in WinList:
            if set(meow) < set(ComInputted):
                return 'COM'                                    #for, else
            elif set(meow) < set(P1Inputted):                   #wowowow
                return 'P1'
        else:
            return 'TIE'
    else:
        for meow in WinList:
            if set(meow) < set(ComInputted):
                return 'COM'
            elif set(meow) < set(P1Inputted):
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
        Win(CheckWin())

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





