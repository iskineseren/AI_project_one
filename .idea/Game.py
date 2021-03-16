import numpy as np
import time
class Game:
    North_index = [1,2,3,4,5,6]
    North_side = [6,5,2,3,40,10]
    #South_index = [1,2,3,4,5,6]
    South_side = [30,13,1,4,4,10]
    Vest_goal = [0]
    East_goal = [0]
    Last_Pit= ['player','area',0,0] # returns the[player, area of the last pit, the index, marbles in pit]
    count = 0
    player = None


    def Board(self): # This create the initial Kalaha board
        print('Pit Index', Game.North_index)
        print('')
        print('         ', Game.North_side)
        print('   V  ', Game.Vest_goal, '                    ', Game.East_goal, '  E ')
        print('         ', Game.South_side)
        print('')




    def UpdateBoard(self, player, move):
        if (player == 'P'):
            #player=player
            PitMarbles = Game.South_side[move - 1] #Get the value of the pit

            count = PitMarbles
            print('Pitmarbles', PitMarbles,'count',count)
            Game.South_side[move - 1] = 0 # replace the number of the pit
            i = 0
            j = 1
            y = 0
            x = 0
            s = 0
            x1=1

            while i < PitMarbles:
                #print('This is i: ',i)
                #print('Move',move)
                if move == 1:
                    count = PitMarbles
                    print(count)
                    Game.continueBoard(count,player)
                    break
                else:
                    nextpit = Game.South_side[(move - 1) - (i + 1)] #Getting the value from the next pit
                    #print('next pit', nextpit)
                    Game.South_side[(move - 1) - (i + 1)] = nextpit + 1 # Adding a marbel to the pit
                    print('i : ', i, 'count : ', count)
                    count = PitMarbles-(i+1)
                    print('count s',count)
                    if i == count:
                        south = 's'
                        Game.Last_Pit=[player,south,(move - 1) - (i + 1),Game.South_side[(move - 1) - (i + 1)]]
                        print('Last pit is',Game.Last_Pit)
                        count = count-(i+1)
                        x=1
                        #print('Last pit is', Last_pit)
                        break
                if Game.South_side[0] == Game.South_side[(move - 1) - (i + 1)]:
                    count = PitMarbles-(i+1)
                    print('i : ', i,'count ', count, 'player is: ', player)
                    Game.continueBoard(count,player)
                    #x=0
                    break
                else:
                    x=1
                i+=1
        elif (player == 'AI'):
            print("AI algorithm begins")
            #player=player
            PitMarbles = Game.North_side[move - 1] #Get the value of the pit

            count = PitMarbles
            print('Pitmarbles AI', PitMarbles,'count',count, 'move',move)
            Game.North_side[move - 1] = 0 # replace the number of the pit
            i = 0
            x = 0
            while i < PitMarbles:
            #print('This is i: ',i)
                print('Move',move)
                if move == 6:
                    count = PitMarbles
                    print('Lastpit',count)
                    Game.continueBoardAI(count,player)
                    break
                else:
                    nextpit = Game.North_side[(move - 1) + (i + 1)] #Getting the value from the next pit
                    print('next pit', nextpit)
                    Game.North_side[(move - 1) + (i + 1)] = nextpit + 1 # Adding a marbel to the pit
                    print('i : ', i, 'count : ', count)
                    count = PitMarbles-(i+1)
                    print('count s',count)
                    if 0 == count:
                        north = 'n'
                        Game.Last_Pit=[player,north,(move - 1) + (i + 1),Game.North_side[(move - 1) + (i + 1)]]
                        print('Last pit is',Game.Last_Pit)
                        count = count-(i+1)
                        x=1
                        #print('Last pit is', Last_pit)
                        break
                if Game.North_side[5] == Game.North_side[(move - 1) + (i + 1)]:
                    count = PitMarbles-(i+1)
                    print('i : ', i,'count ', count, 'player is: ', player)
                    Game.continueBoardAI(count,player)
                    #x=0
                    break
                else:
                    x=1
                i+=1
                    ##End of new method tryout




    def continueBoard(count,player):
        i = 0
        x = 0
        s = 0
        x1=1
        print('player in method ', player, "count in method: ", count)
        count=count
        while count > 0:

         while x <1 :
            vGoal = Game.Vest_goal[0] # Getting the values in the Vest goal
            #print('Vest goal :', vGoal)
            Game.Vest_goal[0] = vGoal + 1  # Adding a marble to the Vest Goal
            VGoal2 = Game.Vest_goal[0]
            #print('value Vest goal', VGoal2,'This is x: ',x)
            #if Game.Vest_goal[0]==Game.Vest_goal[0]:
            count = count-1
            print('goal 1 count',count,'x',x)
            #break
            if count==0:
                goal = 'g'
                Game.Last_Pit=[player,goal,0,Game.Vest_goal[0]]
                print('Last pit is',Game.Last_Pit)
                print('goal count',count)
                #print('Last pit is', Last_pit)
                break
            x +=1

         while s < count:
            nextpit = Game.North_side[s] #Getting the value from the next pit
            print('Northside', nextpit,'s:',s, 'count',count)
            Game.North_side[s]  = nextpit + 1
            if (s+1) == count:
                north = 'n'
                Game.Last_Pit=[player,north,s,Game.North_side[s]]
                count = count-(s+1)
                print('Last pit is',Game.Last_Pit)
                print('count is N1', count)
                break
            if Game.North_side[0 + s] == Game.North_side[5]:
                count = count-(s+1)
                print('End of North side method. count: ',count,'s:',s)
                s=0
                break
            s += 1
         while i < count:
            nextpit = Game.South_side[5 - i] #Getting the value from the next pit
            print('South side method i: ', i ,'count :', count)
            Game.South_side[5 - i] = nextpit + 1 # Adding a marbel to the pit
            if i+1 == count:
                south = 's'
                Game.Last_Pit=[player,south,(5-i),Game.South_side[5 - i]]
                count = count-(i+1)
                print('Last pit is method',Game.Last_Pit, 'count s', count)
                x=1
                #print('Last pit is', Last_pit)
                break
            if Game.South_side[0] == Game.South_side[5 - i]:
                count = count-(i+1)
                print('south method: ', i,' count : ',count )
                i=0
                x=0
                break
            i+=1


    def continueBoardAI(count,player):
        i = 0
        x = 0
        s = 0
        print('player in method ', player, "count in method: ", count)
        #count = count
        while count > 0:
            print('count in first while', count)
            while x <1 :
                vGoal = Game.East_goal[0] # Getting the values in the Vest goal
                #print('Vest goal :', vGoal)
                Game.East_goal[0] = vGoal + 1  # Adding a marble to the Vest Goal
                VGoal2 = Game.East_goal[0]
                print('value East goal', VGoal2,'This is x: ',x)
                #if Game.Vest_goal[0]==Game.Vest_goal[0]:
                count = count-1
                print('goal East 1 count',count,'x',x)
                #break
                if count==0:
                    goal = 'AIg'
                    Game.Last_Pit=[player,goal,0,Game.East_goal[0]]
                    print('Last pit is',Game.Last_Pit)
                    print('goal count',count)
                    #print('Last pit is', Last_pit)
                    break
                x +=1
            while i < count:
                nextpit = Game.South_side[5 - i] #Getting the value from the next pit
                print('South side method i: ', i ,'count :', count)
                Game.South_side[5 - i] = nextpit + 1 # Adding a marbel to the pit
                if count == 0:
                    south = 's'
                    Game.Last_Pit=[player,south,(5-i),Game.South_side[5 - i]]
                    count = count-(i+1)
                    print('Last pit is method',Game.Last_Pit, 'count s', count)
                    break
                if Game.South_side[0] == Game.South_side[5 - i]:
                    count = count-(i+1)
                    print('Last pit south: ', i,' count : ',count )
                    i=0
                    break
                i+=1
            while s < count:
                nextpit = Game.North_side[s] #Getting the value from the next pit
                print('Northside', nextpit,'s:',s, 'count',count)
                Game.North_side[s]  = nextpit + 1
                if (s+1) == count:
                    north = 'n'
                    Game.Last_Pit=[player,north,s,Game.North_side[s]]
                    count = count-(s+1)
                    print('Last pit is',Game.Last_Pit)
                    print('count is N1', count)
                    x=1
                    break
                if Game.North_side[0 + s] == Game.North_side[5]:
                    count = count-(s+1)
                    print('End of North side method. count: ',count,'s:',s)
                    s=0
                    x=0
                    break
                s += 1

 ## problems with the North update if more then marbles for a board around