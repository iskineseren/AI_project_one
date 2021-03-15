import numpy as np
import time
class Game1:
    North_index = [1,2,3,4,5,6]
    North_side = [6,6,1,3,30,6]
    South_index = [1,2,3,4,5,6]
    South_side = [30,13,1,4,4,10]
    Vest_goal = [0]
    East_goal = [0]
    Last_Pit= ['player','area',0]
    count = 0
    player = None


    def Board(self): # This create the initial Kalaha board
        print('Pit Index', Game1.North_index)
        print('')
        print('         ', Game1.North_side)
        print('   V  ', Game1.Vest_goal, '                ', Game1.East_goal, '  E ')
        print('         ', Game1.South_side)
        print('')




    def UpdateBoard(self, player, move):
        if (player == 'P'):
            #player=player
            PitMarbles = Game1.South_side[move - 1] #Get the value of the pit

            count = PitMarbles
            print('Pitmarbles', PitMarbles,'count',count)
            Game1.South_side[move - 1] = 0 # replace the number of the pit
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
                    Game1.continueBoard(count, player)
                    break
                else:
                    nextpit = Game1.South_side[(move - 1) - (i + 1)] #Getting the value from the next pit
                    #print('next pit', nextpit)
                    Game1.South_side[(move - 1) - (i + 1)] = nextpit + 1 # Adding a marbel to the pit
                    print('i : ', i, 'count : ', count)
                    count = PitMarbles-(i+1)
                    print('count s',count)
                    if i == count:
                        south = 's'
                        Game1.Last_Pit=[player, south, (move - 1) - (i + 1)]
                        print('Last pit is', Game1.Last_Pit)
                        count = count-(i+1)
                        x=1
                        #print('Last pit is', Last_pit)
                        break
                if Game1.South_side[0] == Game1.South_side[(move - 1) - (i + 1)]:
                    count = PitMarbles-(i+1)
                    print('i : ', i,'count ', count, 'player is: ', player)
                    Game1.continueBoard(count, player)
                    #x=0
                    break
                else:
                    x=1
                i+=1
        elif (player == 'AI'):
            print("AI algorithm begins")
            #player=player
            PitMarbles = Game1.North_side[move - 1] #Get the value of the pit

            count = PitMarbles
            print('Pitmarbles AI', PitMarbles,'count',count, 'move',move)
            Game1.North_side[move - 1] = 0 # replace the number of the pit
            i = 0
            x = 0
            while i < PitMarbles:
                #print('This is i: ',i)
                #print('Move',move)
                if move == 6:
                    count = PitMarbles
                    print('Lastpit',count)
                    Game1.continueBoardAI(count, player)
                    break
                else:
                    nextpit = Game1.North_side[(move - 1) + (i + 1)] #Getting the value from the next pit
                    print('next pit', nextpit)
                    Game1.North_side[(move - 1) + (i + 1)] = nextpit + 1 # Adding a marbel to the pit
                    print('i : ', i, 'count : ', count)
                    count = PitMarbles-(i+1)
                    print('count s',count)
                    if i == count:
                        north = 'n'
                        Game1.Last_Pit=[player, north, (move - 1) + (i + 1)]
                        print('Last pit is', Game1.Last_Pit)
                        count = count-(i+1)
                        x=1
                        #print('Last pit is', Last_pit)
                        break
                if Game1.North_side[5] == Game1.North_side[(move - 1) + (i + 1)]:
                    count = PitMarbles-(i+1)
                    print('i : ', i,'count ', count, 'player is: ', player)
                    Game1.continueBoardAI(count, player)
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
                vGoal = Game1.Vest_goal[0] # Getting the values in the Vest goal
                #print('Vest goal :', vGoal)
                Game1.Vest_goal[0] = vGoal + 1  # Adding a marble to the Vest Goal
                VGoal2 = Game1.Vest_goal[0]
                #print('value Vest goal', VGoal2,'This is x: ',x)
                #if Game1.Vest_goal[0]==Game1.Vest_goal[0]:
                count = count-1
                print('goal 1 count',count,'x',x)
                #break
                if count==0:
                    goal = 'g'
                    Game1.Last_Pit=[player, goal, 0]
                    print('Last pit is', Game1.Last_Pit)
                    print('goal count',count)
                    #print('Last pit is', Last_pit)
                    break
                x +=1

            while s < count:
                nextpit = Game1.North_side[s] #Getting the value from the next pit
                print('Northside', nextpit,'s:',s, 'count',count)
                Game1.North_side[s]  = nextpit + 1
                if (s+1) == count:
                    north = 'n'
                    Game1.Last_Pit=[player, north, s]
                    count = count-(s+1)
                    print('Last pit is', Game1.Last_Pit)
                    print('count is N1', count)
                    break
                if Game1.North_side[0 + s] == Game1.North_side[5]:
                    count = count-(s+1)
                    print('End of North side method. count: ',count,'s:',s)
                    s=0
                    break
                s += 1
            while i < count:
                nextpit = Game1.South_side[5 - i] #Getting the value from the next pit
                print('South side method i: ', i ,'count :', count)
                Game1.South_side[5 - i] = nextpit + 1 # Adding a marbel to the pit
                if i+1 == count:
                    south = 's'
                    Game1.Last_Pit=[player, south, (5 - i)]
                    count = count-(i+1)
                    print('Last pit is method', Game1.Last_Pit, 'count s', count)
                    x=1
                    #print('Last pit is', Last_pit)
                    break
                if Game1.South_side[0] == Game1.South_side[5 - i]:
                    count = count-(i+1)
                    print('south method: ', i,' count : ',count )
                    i=0
                    x=0
                    break
                i+=1


    def continueBoardAI(count,player):
        i = 0
