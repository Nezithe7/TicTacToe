# TicTacToe
===============================================================================

V0 beta

-CheckWin failing sometimes

===============================================================================

V1

-Finally working, full game
-Proud of CheckWin() function that is working (used for,else)
-COmputer randomly selects which square to use
-Code to ask the player if they want to TryAgain is under progress

===============================================================================

V2

-TryAgain is working
-Strategy for Computer is under progress

#Comments 23/10/17
  "Random" error occuring
	TryAgain is not working 
	Gave up on V2, going to work on strategy for com on V3
  
#Resolved
	Error on line: "Spaces[int(ComInput)] = 'O'"
	Due to trying: "ComInput = ComputerSmartChoice()"
	(Function had not been completed yet)

===============================================================================

V3  Started 23/10/17

-TryAgain Not worked on
-Strategy for Computer UP AND RUNNING 
-Will now show which box is which number on the board ("ShowNumberBoard()")

#Comments 23/10/17
	Program randomly adding 2x of the index to "ComInputted" idk why
	Tiny script to fix above problem caused a "ComInputted referenced before assignment" error
	Fixed with global ComInputted (No Good)
  
#Resolved
	Not adding 2x of index to "ComInputted" anymore, no idea what I changed
	Should probably work on V4 instead, the complete rewrite, maybe in C++

- Going to have to rewrite the whole code in a more neat manner
	- Include main() function and not call other functions repeatedly as in the last few versions
	- Use more efficient techniques
		- More arguments instead of global variables
    - Classes maybe
===============================================================================
V99 (Ideas for the future)

-Let the player choose how large the Tic Tac Toe board will be
	=(Find an algorithm to find the elements in WinList)
  =(Find an algorithm to print board)
-2-player game
	=PvP
