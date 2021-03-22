import numpy as np


# import Player
class AIGame:
    North_index = [1, 2, 3, 4, 5, 6]
    North_side = [2, 3, 1, 1, 1, 1]
    South_side = [6, 6, 6, 6, 6, 6]
    Vest_goal = [0]
    East_goal = [0]
    Last_Pit = ['player', 'area', 0, 0]  # returns the[player, area of the last pit, the index, marbles in pit]
    count = 0
    player = None
    South_side_status = 1
    North_side_status = 1

    def Board(self):  # This create the initial Kalaha board
        print('Pit Index     ', AIGame.North_index)
        print('')
        print('              ', AIGame.North_side)
        print('Your goal', AIGame.Vest_goal, '                    ', AIGame.East_goal, '  AI Goal ')
        print('              ', AIGame.South_side)
        print('')

    def UpdateBoard(self, player, move):
        if (player == 'P'):
            # player=player
            PitMarbles = AIGame.South_side[move - 1]  # Get the value of the pit

            count = PitMarbles
            # print('Pitmarbles', PitMarbles,'count',count)
            AIGame.South_side[move - 1] = 0  # replace the number of the pit
            i = 0
            while True:
                # print('This is i: ',i)
                # print('Move',move)
                if move == 1:
                    # count = PitMarbles
                    # print(count)
                    AIGame.continueBoard(count, player)
                    return False
                    break
                else:
                    nextpit = AIGame.South_side[(move - 1) - (i + 1)]  # Getting the value from the next pit
                    # print('next pit', nextpit)
                    AIGame.South_side[(move - 1) - (i + 1)] = nextpit + 1  # Adding a marbel to the pit
                    # count = PitMarbles-(i+1)
                    # print('i : ', i,'count south first',count)
                    if count == (1 + i):
                        south = 's'
                        AIGame.Last_Pit = [player, south, (move - 1) - (i + 1), AIGame.South_side[(move - 1) - (i + 1)]]
                        m = AIGame()
                        m.CheckLastMarble()
                        m.checkSideStatus()
                        count = count - (i + 1)
                        # x=1
                        # print('Last pit is', Last_pit)
                        break
                if (move - 1) - (i + 1) == 0:
                    count = PitMarbles - (i + 1)
                    # print('end south first i : ', i,'count ', count, 'player is: ', player)
                    AIGame.continueBoard(count, player)
                    # x=0
                    break
                # else:
                # x=1
                i += 1
        elif (player == 'AI'):
            # print("AI algorithm begins")
            # player=player
            PitMarbles = AIGame.North_side[move - 1]  # Get the value of the pit

            count = PitMarbles
            # print('Pitmarbles AI', PitMarbles,'count',count, 'move',move)
            AIGame.North_side[move - 1] = 0  # replace the number of the pit
            i = 0
            x = 0
            while True:
                # print('This is i: ',i)
                # print('Move',move)
                if move == 6:
                    # count = PitMarbles
                    # print('Lastpit',count)
                    AIGame.continueBoardAI(count, player)
                    return False
                    break
                else:
                    nextpit = AIGame.North_side[(move - 1) + (i + 1)]  # Getting the value from the next pit
                    # print('next pit', nextpit)
                    AIGame.North_side[(move - 1) + (i + 1)] = nextpit + 1  # Adding a marbel to the pit
                    # print('i : ', i, 'count : ', count)
                    # count = PitMarbles-(i+1)
                    # print('count north first',count)
                    if count == (i + 1):
                        north = 'n'
                        AIGame.Last_Pit = [player, north, (move - 1) + (i + 1), AIGame.North_side[(move - 1) + (i + 1)]]
                        # print('Last marble landed', AIGame.Last_Pit)
                        m = AIGame()
                        m.CheckLastMarble()
                        m.checkSideStatus()
                        count = count - (i + 1)
                        # x=1
                        # print('Last pit is', Last_pit)
                        break
                    elif (move - 1) + (i + 1) == 5:
                        count = PitMarbles - (i + 1)
                        # print('ended north side continueBoardAI: i', i,'count ', count, 'player is: ', player)
                        AIGame.continueBoardAI(count, player)
                        # x=0
                        break
                    # else:
                    # x=1
                    i += 1
                ##End of new method tryout

    def continueBoard(count, player):
        i = 0
        x = 0
        s = 0
        # print('player in method ', player, "count in method: ", count)
        while count > 0:
            while x < 1:
                vGoal = AIGame.Vest_goal[0]  # Getting the values in the Vest goal
                # print('Vest goal :', vGoal)
                AIGame.Vest_goal[0] = vGoal + 1  # Adding a marble to the Vest Goal
                VGoal2 = AIGame.Vest_goal[0]
                # print('value Vest goal', VGoal2,'This is x: ',x)
                # if AIGame.Vest_goal[0]==AIGame.Vest_goal[0]:
                count = count - 1
                # print('goal 1 count',count,'x',x)
                # break
                if count == 0:
                    goal = 'g'
                    AIGame.Last_Pit = [player, goal, 0, AIGame.Vest_goal[0]]
                    m = AIGame()
                    m.CheckLastMarble()
                    m.checkSideStatus()
                    # print('Last marble in vestgoal', AIGame.Last_Pit)
                    # print('goal count',count)
                    # print('Last pit is', Last_pit)
                    break
                x += 1

            while s < count:
                nextpit = AIGame.North_side[s]  # Getting the value from the next pit
                # print('Northside', nextpit,'s:',s, 'count',count)
                AIGame.North_side[s] = nextpit + 1
                # count = count-(s+1)
                if count == (s + 1):
                    north = 'n'
                    AIGame.Last_Pit = [player, north, s, AIGame.North_side[s]]
                    m = AIGame()
                    m.CheckLastMarble()
                    m.checkSideStatus()
                    count = count - (s + 1)
                    # x=1
                    # print('Last marble in north side', AIGame.Last_Pit, 'count: ', count)
                    break
                if (s + 1) == 6:  # something wrong with this I think...
                    count = count - (s + 1)
                    # print('End of North side method. count: ',count,'s:',s)
                    s = 0
                    break
                s += 1
            while i < count:
                nextpit = AIGame.South_side[5 - i]  # Getting the value from the next pit
                AIGame.South_side[5 - i] = nextpit + 1  # Adding a marbel to the pit
                # count = count-(i+1)
                # print('South side method i: ', i ,'count :', count)
                if count == (i + 1):
                    south = 's'
                    AIGame.Last_Pit = [player, south, (5 - i), AIGame.South_side[5 - i]]
                    m = AIGame()
                    m.CheckLastMarble()
                    m.checkSideStatus()
                    count = count - (i + 1)
                    # print('Last marble on south side', AIGame.Last_Pit, 'count s', count)
                    x = 1
                    # print('Last pit is', Last_pit)
                    break
                if (i + 1) == 6:
                    # count = count-(i+1)
                    # print('south end: ', i,' count : ',count, 'lastindex',AIGame.South_side[5 - i] )
                    i = 0
                    x = 0
                    break
                i += 1

    def continueBoardAI(count, player):
        i = 0
        x = 0
        s = 0
        # print('player in method ', player, "count in method: ", count)
        # count = count
        while count > 0:
            # print('count in first while', count)
            while x < 1:
                vGoal = AIGame.East_goal[0]  # Getting the values in the Vest goal
                # print('Vest goal :', vGoal)
                AIGame.East_goal[0] = vGoal + 1  # Adding a marble to the Vest Goal
                VGoal2 = AIGame.East_goal[0]
                # print('value East goal', VGoal2,'This is x: ',x)
                # if AIGame.Vest_goal[0]==AIGame.Vest_goal[0]:
                count = count - 1
                # print('goal East 1 count',count,'x',x)
                # break
                if count == 0:
                    goal = 'AIg'
                    AIGame.Last_Pit = [player, goal, 0, AIGame.East_goal[0]]
                    m = AIGame()
                    m.CheckLastMarble()
                    m.checkSideStatus()
                    # print('Last marble in East goal', AIGame.Last_Pit)
                    # print('goal count',count)
                    # print('Last pit is', Last_pit)
                    break
                x += 1
            while i < count:
                nextpit = AIGame.South_side[5 - i]  # Getting the value from the next pit
                # print('South side method AI i: ', i ,'count :', count, 'nextpit: ', nextpit)
                AIGame.South_side[5 - i] = nextpit + 1  # Adding a marbel to the pit
                # count = count-(i+1)
                if count == (i + 1):
                    south = 's'
                    AIGame.Last_Pit = [player, south, (5 - i), AIGame.South_side[5 - i]]
                    m = AIGame()
                    m.CheckLastMarble()
                    m.checkSideStatus()
                    count = count - (i + 1)
                    # print('Last marble in south side', AIGame.Last_Pit, 'count', count)
                    break
                elif (i + 1) == 6:
                    count = count - (i + 1)
                    # print('End of south: i: ', i,' count : ',count, 'Lastindex is', AIGame.South_side[i-5] )
                    break
                i += 1
            while s < count:
                nextpit = AIGame.North_side[s]  # Getting the value from the next pit
                # print('Northside', nextpit,'s:',s, 'count',count)
                AIGame.North_side[s] = nextpit + 1
                if (s + 1) == count:
                    north = 'n'
                    AIGame.Last_Pit = [player, north, s, AIGame.North_side[s]]
                    m = AIGame()
                    m.CheckLastMarble()
                    m.checkSideStatus()
                    count = count - (s + 1)
                    # print('Last pit is', AIGame.Last_Pit)
                    # print('count is N1', count)
                    x = 1
                    break
                if s == 5:
                    count = count - (s + 1)
                    # print('End of North side method. count: ',count,'s:',s)
                    s = 0
                    x = 0
                    break
                s += 1

    # Last_Pit= ['player','area',0,0] # returns the[player, area of the last pit, the index, marbles in pit]

    def CheckLastMarble(self):
        if AIGame.Last_Pit[0] == 'AI' and AIGame.Last_Pit[1] == 'n' and AIGame.Last_Pit[3] == 1:
            print('AI can take the opposite marbles from index', AIGame.Last_Pit[2])
            oppositeSide = AIGame.South_side[AIGame.Last_Pit[2]]  # Getting the value from the other side
            print('Marbles from opposite side ', oppositeSide)
            AIGame.South_side[AIGame.Last_Pit[2]] = 0  # replacing with zero
            eGoal = AIGame.East_goal[0]  # Getting the values in the Vest goal
            # print('Vest goal :', vGoal)
            AIGame.East_goal[0] = eGoal + oppositeSide  # Adding a marble to the Vest Goal
            eGoal2 = AIGame.East_goal[0]
            print('Original goal', eGoal, 'updated goal ', eGoal2)
        elif AIGame.Last_Pit[0] == 'P' and AIGame.Last_Pit[1] == 's' and AIGame.Last_Pit[3] == 1:
            print('you can take the opposite marbles from index', AIGame.Last_Pit[2])
            oppositeSide = AIGame.North_side[AIGame.Last_Pit[2]]  # Getting the value from the other side
            print('Marbles from opposite side ', oppositeSide)
            AIGame.North_side[AIGame.Last_Pit[2]] = 0  # replacing with zero
            vGoal = AIGame.Vest_goal[0]  # Getting the values in the Vest goal
            # print('Vest goal :', vGoal)
            AIGame.Vest_goal[0] = vGoal + oppositeSide  # Adding a marble to the Vest Goal
            vgoal2 = AIGame.Vest_goal[0]
            print('Original goal', vGoal, 'updated goal ', vgoal2)
        # else:
        #   print('Nothing to take')

    def checkSideStatus(self):
        y1 = 0  # Sum of marbles in south side
        y2 = 0  # Sum of marbles in North side
        x1 = 0
        x2 = 0
        i = 0
        for x1 in AIGame.South_side:
            y1 = y1 + x1
        for x2 in AIGame.North_side:
            y2 = y2 + x2
        # print(y1, y2)

        if (y1 == 0):
            print('You have no more marbles on your side. Game is finished')
            AIGame.North_side_status = 0
            AIGame.South_side_status = 0
            while i < 6:
                oppositeSide = AIGame.North_side[i]  # Getting the value from the other side
                # print('Marbles from opposite side ', oppositeSide)
                AIGame.North_side[i] = 0  # replacing with zero
                vGoal = AIGame.East_goal[0]  # Getting the values in the Vest goal
                AIGame.East_goal[0] = vGoal + oppositeSide  # Adding a marble to the Vest Goal
                VGoal2 = AIGame.East_goal[0]
                # print('Original goal',vGoal,'updated goal ', VGoal2)
                i += 1
        elif (y2 == 0):
            AIGame.North_side_status = 0
            AIGame.South_side_status = 0
            while i < 6:
                oppositeSide = AIGame.South_side[i]  # Getting the value from the other side
                # print('Marbles from opposite side ', oppositeSide)
                AIGame.South_side[i] = 0  # replacing with zero
                vGoal = AIGame.Vest_goal[0]  # Getting the values in the Vest goal
                # print('Vest goal :', vGoal)
                AIGame.Vest_goal[0] = vGoal + oppositeSide  # Adding a marble to the Vest Goal
                VGoal2 = AIGame.Vest_goal[0]
                # print('Original goal',vGoal,'updated goal ', VGoal2)
                i += 1
        else:
            # print('The game is still on y1: ', y1,'y2: ', y2)
            AIGame.South_side_status = y1
            AIGame.North_side_status = y2
