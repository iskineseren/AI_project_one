import numpy as np
import time
class Kalaha:
    player = None

    def NewBoard(self): # This create the initial Kalaha board
     North_index = [1,2,3,4,5,6]
     North_side = [6,6,6,6,6,6,]
     South_index = [1,2,3,4,5,6]
     South_side = [6,6,6,6,6,6]
     Vest_goal = [0]
     East_goal = [0]

     print('Pit Index', North_index)
     print('')
     print('         ', North_side)
     print('   V  ', Vest_goal,'                ',East_goal, '  E ')
     print('         ', South_side)
     print('')



    def WhoBegins( player): # This methods decide who begins based on user input
     startplayer = input("Would you like to play? (Y/N)")
     if (startplayer.lower() == 'y'):
            print("You begin. Choose a pit from your side and type index number")
            player = 'P'
     elif (startplayer.lower() == 'n'):
            print("Computer begins")
            player = 'AI'


Game = Kalaha()
Game.NewBoard()
Game.WhoBegins()
