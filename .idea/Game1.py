import numpy as np
import time
class Game1:


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

