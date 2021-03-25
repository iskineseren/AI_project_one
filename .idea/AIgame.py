import numpy as np
import Game1

class AIgame:
    Last_Pit= ['player','area',0,0] # returns the[player, area of the last pit, the index, marbles in pit]
    child = []
    count = 0
    player = None
    index = [1,2,3,4,5,6]
    South_side_status = 1
    North_side_status =1

    def state(self, north, south, vest, east,player):
        print('Pit Index     ', AIgame.index)
        print('')
        print('              ', north)
        print('Your goal', vest, '                    ', east, '  AI Goal ')
        print('              ', south)
        print('')
        obj = [north,south,vest,east,player]
        AIgame.child=obj
    


    def UpdateBoardAI(self, player, state ,move):
        state = state
        n1 = state[0]
        n=[]
        for x in n1:
          n.append(x)
        s1 = state[1]
        s=[]
        for x in s1:
            s.append(x)
        v1 = state[2]
        v = []
        for x in v1:
            v.append(x)
        e1 = state[3]
        e = []
        for x in e1:
            e.append(x)
        print(n,s,v,e)

        if (player == 'P'):
            #player=player
            PitMarbles = s[move - 1] #Get the value of the pit

            count = PitMarbles
            #print('Pitmarbles', PitMarbles,'count',count)
            s[move - 1] = 0 # replace the number of the pit
            i = 0
            while True:
                #print('This is i: ',i)
                #print('Move',move)
                if move == 1:
                    #count = PitMarbles
                    #print(count)
                    AIgame.continueBoard(count, player,n, s, v, e)
                    return False
                    break
                else:
                    nextpit = s[(move - 1) - (i + 1)] #Getting the value from the next pit
                    #print('next pit', nextpit)
                    s[(move - 1) - (i + 1)] = nextpit + 1 # Adding a marbel to the pit
                    #count = PitMarbles-(i+1)
                    #print('i : ', i,'count south first',count)
                    if count == (1+i):
                        south = 's'
                        AIgame.Last_Pit=[player, south, (move - 1) - (i + 1), s[(move - 1) - (i + 1)]]
                        m=AIgame()
                        m.CheckLastMarble(n, s, v, e)
                        m.checkSideStatus(n, s, v, e)
                        m.state(n, s, v, e,player)
                        count = count-(i+1)
                        #x=1
                        #print('Last pit is', Last_pit)
                        break
                if (move-1)-(i+1) == 0:
                    count = PitMarbles-(i+1)
                    #print('end south first i : ', i,'count ', count, 'player is: ', player)
                    AIgame.continueBoard(count, player,n, s, v, e)
                    #x=0
                    break
                #else:
                #x=1
                i+=1
        elif (player == 'AI'):
            #print("AI algorithm begins")
            #player=player

            PitMarbles = n[move - 1] #Get the value of the pit
            count = PitMarbles
            #print('Pitmarbles AI', PitMarbles,'count',count, 'move',move, 'nortside', n)
            n[move - 1] = 0 # replace the number of the pit
            i = 0
            x = 0
            while True:
                #print('This is i: ',i)
                #print('Move',move)
                if move == 6:
                    #count = PitMarbles
                    #print('Lastpit',count)
                    AIgame.continueBoardAI(count, player, n, s, v, e)
                    return False
                    break
                else:
                    nextpit = n[(move - 1) + (i + 1)] #Getting the value from the next pit
                    #print('next pit', nextpit)
                    n[(move - 1) + (i + 1)] = nextpit + 1 # Adding a marbel to the pit
                    #print('i : ', i, 'count : ', count)
                    #count = PitMarbles-(i+1)
                    #print('count north first',count)
                    if count == (i+1):
                        north = 'n'
                        AIgame.Last_Pit=[player, north, (move - 1) + (i + 1), n[(move - 1) + (i + 1)]]
                        #print('Last marble landed', AIgame.Last_Pit)
                        #print('Put the side values in the child', AIgame.child)
                        m=AIgame()
                        m.CheckLastMarble(n, s, v, e)
                        m.checkSideStatus(n, s, v, e)
                        m.state(n, s, v, e,player)
                        count = count-(i+1)
                        #x=1
                        #print('Last pit is', Last_pit)
                        break
                    elif (move-1)+(i+1) == 5:
                        count = PitMarbles-(i+1)
                        #print('ended north side continueBoardAI: i', i,'count ', count, 'player is: ', player)
                        AIgame.continueBoardAI(count, player,n, s, v, e)
                        #x=0
                        break
                    #else:
                    #x=1
                    i+=1

                ##End of new method tryout

    def continueBoard(count,player, North_side, South_side, Vest_goal, East_goal):
        i = 0
        x = 0
        s = 0
        #print('player in method ', player, "count in method: ", count)
        while count > 0:
            while x <1 :
                vGoal = Vest_goal[0] # Getting the values in the Vest goal
                #print('Vest goal :', vGoal)
                Vest_goal[0] = vGoal + 1  # Adding a marble to the Vest Goal
                VGoal2 = Vest_goal[0]
                #print('value Vest goal', VGoal2,'This is x: ',x)
                #if AIgame.Vest_goal[0]==AIgame.Vest_goal[0]:
                count = count-1
                #print('goal 1 count',count,'x',x)
                #break
                if count==0:
                    goal = 'g'
                    AIgame.Last_Pit=[player, goal, 0, Vest_goal[0]]
                    m=AIgame()
                    m.CheckLastMarble(North_side, South_side, Vest_goal, East_goal)
                    m.checkSideStatus(North_side, South_side, Vest_goal, East_goal)
                    m.state(North_side, South_side, Vest_goal, East_goal,player)
                    #print('Last marble in vestgoal', AIgame.Last_Pit)
                    #print('goal count',count)
                    #print('Last pit is', Last_pit)
                    break
                x +=1

            while s < count:
                nextpit = North_side[s] #Getting the value from the next pit
                #print('Northside', nextpit,'s:',s, 'count',count)
                North_side[s]  = nextpit + 1
                #count = count-(s+1)
                if count == (s+1):
                    north = 'n'
                    AIgame.Last_Pit=[player, north, s, North_side[s]]
                    m=AIgame()
                    m.CheckLastMarble(North_side, South_side, Vest_goal, East_goal)
                    m.checkSideStatus(North_side, South_side, Vest_goal, East_goal)
                    m.state(North_side, South_side, Vest_goal, East_goal,player)
                    count = count-(s+1)
                    #x=1
                    #print('Last marble in north side', AIgame.Last_Pit, 'count: ', count)
                    break
                if (s+1)==6:# something wrong with this I think...
                    count = count-(s+1)
                    #print('End of North side method. count: ',count,'s:',s)
                    s=0
                    break
                s += 1
            while i < count:
                nextpit = South_side[5 - i] #Getting the value from the next pit
                South_side[5 - i] = nextpit + 1 # Adding a marbel to the pit
                #count = count-(i+1)
                #print('South side method i: ', i ,'count :', count)
                if count == (i+1):
                    south = 's'
                    AIgame.Last_Pit=[player, south, (5 - i), South_side[5 - i]]
                    m=AIgame()
                    m.CheckLastMarble(North_side, South_side, Vest_goal, East_goal)
                    m.checkSideStatus(North_side, South_side, Vest_goal, East_goal)
                    m.state(North_side, South_side, Vest_goal, East_goal,player)
                    count = count-(i+1)
                    #print('Last marble on south side', AIgame.Last_Pit, 'count s', count)
                    x=1
                    #print('Last pit is', Last_pit)
                    break
                if (i+1) == 6:
                    #count = count-(i+1)
                    #print('south end: ', i,' count : ',count, 'lastindex',AIgame.South_side[5 - i] )
                    i=0
                    x=0
                    break
                i += 1


    def continueBoardAI(count,player,North_side, South_side, Vest_goal, East_goal):
        i = 0
        x = 0
        s = 0
        #print('player in method ', player, "count in method: ", count)
        #count = count
        while count > 0:
            #print('count in first while', count)
            while x <1 :
                vGoal = East_goal[0] # Getting the values in the Vest goal
                #print('Vest goal :', vGoal)
                East_goal[0] = vGoal + 1  # Adding a marble to the Vest Goal
                VGoal2 = East_goal[0]
                #print('value East goal', VGoal2,'This is x: ',x)
                #if AIgame.Vest_goal[0]==AIgame.Vest_goal[0]:
                count = count-1
                #print('goal East 1 count',count,'x',x)
                #break
                if count==0:
                    goal = 'AIg'
                    AIgame.Last_Pit=[player, goal, 0, East_goal[0]]
                    m=AIgame()
                    m.CheckLastMarble(North_side, South_side, Vest_goal, East_goal)
                    m.checkSideStatus(North_side, South_side, Vest_goal, East_goal)
                    m.state(North_side, South_side, Vest_goal, East_goal,player)
                    print('Last marble in East goal', AIgame.Last_Pit)
                    #print('goal count',count)
                    #print('Last pit is', Last_pit)
                    break
                x +=1
            while i < count:
                nextpit = South_side[5 - i] #Getting the value from the next pit
                #print('South side method AI i: ', i ,'count :', count, 'nextpit: ', nextpit)
                South_side[5 - i] = nextpit + 1 # Adding a marbel to the pit
                #count = count-(i+1)
                if count==(i+1):
                    south = 's'
                    AIgame.Last_Pit=[player, south, (5 - i), South_side[5 - i]]
                    m=AIgame()
                    m.CheckLastMarble(North_side, South_side, Vest_goal, East_goal)
                    m.checkSideStatus(North_side, South_side, Vest_goal, East_goal)
                    m.state(North_side, South_side, Vest_goal, East_goal,player)
                    count = count-(i+1)
                    print('Last marble in south side', AIgame.Last_Pit, 'count', count)
                    break
                elif (i+1) == 6:
                    count = count-(i+1)
                    #print('End of south: i: ', i,' count : ',count, 'Lastindex is', AIgame.South_side[i-5] )
                    break
                i+=1
            while s < count:
                nextpit = North_side[s] #Getting the value from the next pit
                print('Northside', nextpit,'s:',s, 'count',count)
                North_side[s]  = nextpit + 1
                if (s+1) == count:
                    north = 'n'
                    AIgame.Last_Pit=[player, north, s, North_side[s]]
                    m=AIgame()
                    m.CheckLastMarble(North_side, South_side, Vest_goal, East_goal)
                    m.checkSideStatus(North_side, South_side, Vest_goal, East_goal)
                    m.state(North_side, South_side, Vest_goal, East_goal,player)
                    count = count-(s+1)
                    #print('Last pit is', AIgame.Last_Pit)
                    #print('count is N1', count)
                    x=1
                    break
                if s == 5:
                    count = count-(s+1)
                    #print('End of North side method. count: ',count,'s:',s)
                    s=0
                    x=0
                    break
                s+=1


    #Last_Pit= ['player','area',0,0] # returns the[player, area of the last pit, the index, marbles in pit]

    def CheckLastMarble(self,North_side, South_side, Vest_goal, East_goal):
        if AIgame.Last_Pit[0] == 'AI' and AIgame.Last_Pit[1]== 'n' and AIgame.Last_Pit[3]==1:
            print('AI can take the opposite marbles from index', AIgame.Last_Pit[2])
            oppositeSide = South_side[AIgame.Last_Pit[2]] #Getting the value from the other side
            print('Marbles from opposite side ', oppositeSide)
            South_side[AIgame.Last_Pit[2]] = 0 # replacing with zero
            eGoal = East_goal[0] # Getting the values in the Vest goal
            #print('Vest goal :', vGoal)
            East_goal[0] = eGoal + oppositeSide  # Adding a marble to the Vest Goal
            eGoal2 = East_goal[0]
            print('Original goal',eGoal,'updated goal ', eGoal2)
        elif AIgame.Last_Pit[0] == 'P' and AIgame.Last_Pit[1]== 's' and AIgame.Last_Pit[3]==1:
            print('you can take the opposite marbles from index', AIgame.Last_Pit[2])
            oppositeSide = North_side[AIgame.Last_Pit[2]] #Getting the value from the other side
            print('Marbles from opposite side ', oppositeSide)
            North_side[AIgame.Last_Pit[2]] = 0 # replacing with zero
            vGoal = Vest_goal[0] # Getting the values in the Vest goal
            #print('Vest goal :', vGoal)
            Vest_goal[0] = vGoal + oppositeSide  # Adding a marble to the Vest Goal
            VGoal2 = Vest_goal[0]
            print('Original goal',vGoal,'updated goal ', VGoal2)
        #else:
        #   print('Nothing to take')


    def checkSideStatus(self,North_side, South_side, Vest_goal, East_goal):
        y1=0 #Sum of marbles in south side
        y2=0 # Sum of marbles in North side
        x1=0
        x2=0
        i=0
        for x1 in South_side:
            y1=y1+x1
        for x2 in North_side:
            y2 = y2+x2
        #print(y1, y2)

        if (y1 ==0):
            print('You have no more marbles on your side. Game is finished')
            North_side_status = 0
            South_side_status = 0
            while  i < 6:
                oppositeSide = North_side[i] #Getting the value from the other side
                #print('Marbles from opposite side ', oppositeSide)
                North_side[i] = 0 # replacing with zero
                vGoal = East_goal[0] # Getting the values in the Vest goal
                East_goal[0] = vGoal + oppositeSide  # Adding a marble to the Vest Goal
                VGoal2 = East_goal[0]
                #print('Original goal',vGoal,'updated goal ', VGoal2)
                i +=1
        elif (y2 == 0):
            North_side_status = 0
            South_side_status = 0
            while  i < 6:
                oppositeSide = South_side[i] #Getting the value from the other side
                #print('Marbles from opposite side ', oppositeSide)
                South_side[i] = 0 # replacing with zero
                vGoal = Vest_goal[0] # Getting the values in the Vest goal
                #print('Vest goal :', vGoal)
                Vest_goal[0] = vGoal + oppositeSide  # Adding a marble to the Vest Goal
                VGoal2 = Vest_goal[0]
                #print('Original goal',vGoal,'updated goal ', VGoal2)
                i +=1
        else:
            #print('The game is still on y1: ', y1,'y2: ', y2)
            South_side_status = y1
            North_side_status = y2

    def genChildGames(self,state,move):
        #[n,s,v,e]
        #genChildGames(GameState, AI_Index)
        n1 = state[0]
        n=[]
        for x in n1:
        #print(x)
            n.append(x)
        s1 = state[1]
        s = []
        for x in s1:
         s.append(x)
        v1 = state[2]
        v = []
        for x in v1:
            v.append(x)
        e1 = state[3]
        e = []
        for x in e1:
            e.append(x)
            break
        state = [n,s,v,e, state[4]]
        print('state before child',state)
        move = move+1
        print('this is the move', move)
        Game = AIgame()
        Game.UpdateBoardAI(state[4], state,move)
        child = AIgame.child
            # update player:
            # Last_Pit= ['player','area',0,0] # returns the[player, area of the last pit, the index, marbles in pit]
        if AIgame.Last_Pit[0] == 'AI' and AIgame.Last_Pit[1]== 'AIg':
            child[4] = 'AI'
            # AI gets to go again
        elif AIgame.Last_Pit[0] == 'P' and AIgame.Last_Pit[1]== 'g':
            child[4] = 'P'
            # P gets to go again
        else:   #else change player
            if child[4] == 'AI':
                child[4] = 'P'
            elif child[4] == 'P':
                child[4] = 'AI'
        print('child is:',child)
        return child

        #Game.generateMinchild(leaf)
    # def getInitialstate(self):
    #     #This is the same as Gamestate in MiniMax
    #     G = Game1.Game1()
    #     n1 = G.getNorth()
    #     North_side=[]
    #     for x in n1:
    #         #print(x)
    #         n.append(x)
    #     s1 = G.getSouth()
    #     South_side = []
    #     for x in s1:
    #         s.append(x)
    #     v1 = G.getVest()
    #     Vest_goal = []
    #     for x in v1:
    #         v.append(x)
    #     e1 = G.getEast()
    #     East_goal = []
    #     for x in e1:
    #         e.append(x)
    #     GameState = [North_side,South_side,Vest_goal,East_goal]
    #     return GameState

    # def generateMinchild(self, state,player):
    #     #north,east,south,vest
    #     print('states received to generateMinchild ', state)
    #     state_nodes = len(state)
    #     print('How many states? : ', state_nodes)
    #     #player = 'P'
    #     for x in state:
    #         minchild = x
    #         print('minchild :', minchild)
    #         n1 = minchild[0]
    #         print('State n', n1)
    #         n=[]
    #         for x in n1:
    #             #print(x)
    #             n.append(x)
    #         s1 = minchild[2]
    #         s = []
    #         for x in s1:
    #             s.append(x)
    #         print(s)
    #         v1 = minchild[3]
    #         v = []
    #         for x in v1:
    #             v.append(x)
    #         e1 = minchild[1]
    #         e = []
    #         for x in e1:
    #             e.append(x)
    #             print('inside Minchild n, e, s, v', n, e, s, v)
    #         state = [n,s,v,e]
    #         Game = AIgame()
    #         move = Game.legalMove(state,player)
    #         print('move in childMin', move)
    #     for i in move:
    #         move = (i+1)
    #         print('this is the move', move)
    #         Game = AIgame()
    #         Game.UpdateBoardAI(player, state,move)


    # def legalMove(self, state, player):
    #     move = []
    #     if player=='P':
    #         n=state[0]
    #         print('state north in leagalmove',n)
    #         i=0
    #         while i <5:
    #             x = n[i]
    #             print('marbles in legalmoves P', x)
    #             if x > 0:
    #                 move.append(i+1)
    #                 print ('marbles',x, 'i',i)
    #                 return move
    #             i+=1
    #     elif player=='AI':
    #           s= state[1]
    #           print('state south in leagalmove AI',s)
    #           i=0
    #           while i <5:
    #               x = s[i]
    #               print('marbles are', x)
    #               if i > 0:
    #                 move.append(i+1)
    #                 print ('marbles',x, 'i',i)
    #                 return move
    #               i+=1


# Game = AIgame()
# s=Game.getInitialstate()
# l=Game.generateMaxchild(s,'AI')
