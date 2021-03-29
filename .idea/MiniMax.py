#import Player
import Game1
import AIgame
class MiniMax:

    maxPayofflist = []
    maxpayoffindex = []
    indexToChoose = None
    originalSide = []
    zeropit = []

    def getInitialstate(self):
        #n=[]
        #for x in n1:
         #   n.append(x)
    #This is the same as Gamestate in MiniMax
        North_side = []
        for n in Game1.Game1.North_side:
                North_side.append(n)
        South_side = []
        for s in Game1.Game1.South_side:
                South_side.append(s)
        Vest_goal = []
        for v in Game1.Game1.Vest_goal:
            Vest_goal.append(v)
        East_goal  = []
        for e in Game1.Game1.East_goal:
            East_goal.append(e)
        player = 'AI'
        GameState = [North_side,South_side,Vest_goal,East_goal,player]
        MiniMax.originalSide = North_side
        return GameState

    def clearHistory(self):
        MiniMax.indexToChoose = None
        MiniMax.maxPayofflist = []
        MiniMax.maxpayoffindex = []

    def MINIMAX(self, GameState, depthlimit):
        #GameState = [side_pits,South_side,Vest_goal,East_goal,player]
        # returns index of Pit that AI whoud use for the next move and the next state that gets created by choosing the pit
        #print('')
        #print('')
        #print('*** MINIMAX FUNCTION START')
        #print('inside minimax: state', GameState)
        side_pits = []
        if GameState[4] == 'AI':
            side_pits = GameState[0]
            playerVar = 'AI'
        elif GameState[4] == 'P':
            side_pits = GameState[1]
            playerVar = 'P'
        ai = AIgame.AIgame()
        #depthlimit = 3                                                                              # mimimaxfunction iterates max step
        ChildGames      = []
        heuristicValues = [0]*6

        for AI_Index in range(6):
                #print('AI_Index is:',AI_Index)
                if side_pits[AI_Index]  == 0:
                    ChildGames.append(GameState)
                    if playerVar == 'P':
                        heuristicValues[AI_Index] = -1
                    if playerVar == 'AI':
                        heuristicValues[AI_Index] = -1
                elif side_pits[AI_Index]  > 0:                                                 # for all northern pits with marbles
                    #print('north side in minimax',side_pits[AI_Index])
                    ch = ai.genChildGames(GameState, AI_Index)
                    #print('returned child',ch)
                    ChildGames.append(ch) 		# list with states for each index
                    #print('child received from genchild',ChildGames)
                    #print('AI_Index is ',AI_Index)
                    depth = 0
                    state = ChildGames[AI_Index]
                    checkNorth = state[0]
                    checkEast1 = state[3]
                    #print('east: ',checkEast1)
                    for x in checkEast1:
                         checkEast = int(x)
                    #print('state in minimax',checkNorth)# [0] bc it returns a list inide of a list
                    if sum(checkNorth) ==0 or checkEast>36:
                        MiniMax.indexToChoose = AI_Index
                        #print('index in the end of game: ',MiniMax.indexToChoose)
                    while state[4] == playerVar:                                                         # while AI gets to go again, start new minimax iteration
                        #minimax = MiniMax.MiniMax()
                        depthlimitInWhile = 0
                        state = MiniMax().MINIMAX(state, depthlimitInWhile)[1]
                    heuristicValues[AI_Index] = MiniMax().minValue(GameState, state ,depth, depthlimit,AI_Index)		                # array with payoff for each index
                    #print('heuristicValues in minimax function:', heuristicValues)
                    #print('depht is:', depth)
                    # GameState = actual current state in game
                    # state = ChildGames(AI_Index), calculated belief state
                #end if
            #end for
        # returns index of max payoff -> same than best pit_index to choose from

        indexwithgreatestpayoff = heuristicValues.index(max(heuristicValues))
        maxpayof = heuristicValues[indexwithgreatestpayoff]
        #print('payof index: ',indexwithgreatestpayoff,'Maxpayof', maxpayof)
        nextGameState = ChildGames[heuristicValues.index(max(heuristicValues))]
        #print('MINIMAX FUNCTION DONE')
        #print('Print in minimax: ',indexwithgreatestpayoff, nextGameState)
        return [indexwithgreatestpayoff, nextGameState, MiniMax.indexToChoose]

    def minValue(self, GameState, state, depth, depthlimit,AI_Index):
        #print('')
        #print('')
        #print('*** MIN-VALUE FUNCTION START')
        # returns a utility / heuristic value
        # state = [North_side,South_side,Vest_goal,East_goal,player]
        if state[4] == 'AI':
            side_pits = state[0]
            Own_goal = state[3][0]
            Own_goal_GS = GameState[3][0]
            Opp_goal = state[2][0]  #opponment's goal
            Opp_goal_GS = GameState[2][0]  #opponment's GameState goal
            #print('AI own goal in Min value : ', Own_goal,'Own goal GS', Own_goal_GS, 'Opp goal : ', Opp_goal, 'Opp goal GS ', Opp_goal_GS)
            playerVar = 'AI'
        elif state[4] == 'P':
            side_pits = state[1]
            Own_goal = state[2][0]
            Own_goal_GS = GameState[2][0]
            Opp_goal = state[3][0]  #opponment's goal
            Opp_goal_GS = GameState[3][0]  #opponment's GameState goal
            playerVar = 'P'
        ChildGames_min = []
        heuristicValues = [0]*6
        [terminal, state] = MiniMax().terminalTest(state)
        depth += 1
        if terminal: # or depth == depthlimit:
            heuristicValue = 100									                                # returns positiv value bc max player can finish the game
        elif depth >= depthlimit:
            # huerastic function: (new marbles in own kalaha) - (new marbles in player's kalaha)
            heuristicValue = (Opp_goal - Opp_goal_GS) - (Own_goal - Own_goal_GS)
            #print('heuristicValue in min is:', heuristicValue)
        else:
            for MIN_Index in range(6):
                #print('MIN_Index is:',MIN_Index)
                if side_pits[MIN_Index]  == 0:
                    ChildGames_min.append(state)
                    if playerVar == 'P':
                        heuristicValues[MIN_Index] = -1
                    if playerVar == 'AI':
                        heuristicValues[MIN_Index] = -1
                elif side_pits[MIN_Index]  > 0:
                # for all northern pits with marbles
                    ChildGames_min.append(AIgame.AIgame().genChildGames(state,MIN_Index)) 			                # array with states for each index
                    #print('depth in minvalue:', depth)
                    MIN_state = ChildGames_min[MIN_Index]
                    while MIN_state[4] == playerVar:                                          # while Player gets to go again, start new minimax iteration (in this recursion player is max, AI is min)
                        #minimax = MiniMax.MiniMax()
                        depthlimitInWhile = 0
                        MIN_state = MiniMax().MINIMAX(MIN_state, depthlimitInWhile)[1]
                        #print('state minstate', MIN_state)# save new_MINMAX-nextGameState as 'state' to continue original MINMAX
                    heuristicValues[MIN_Index] = MiniMax().maxValue(GameState, MIN_state, depth, depthlimit,AI_Index)				        # array with payoff for each index
                    #print('heuristicValues in min function:', heuristicValues)
            #end for
            heuristicValue = min(heuristicValues) #gets only updated after 'else' part is ealuated
        #end if
        return heuristicValue


    def maxValue(self, GameState, state, depth, depthlimit, AI_Index):
        #print('*** MAX VALUE FUNCTION START')
        #print('')
        #print('')
        # returns a utility / heuristic value
        # state = [North_side,South_side,Vest_goal,East_goal,player]

        if state[4] == 'AI':
            side_pits = state[0]
            Own_goal = state[3][0]
            Own_goal_GS = GameState[3][0]
            Opp_goal = state[2][0]  #opponment's goal
            Opp_goal_GS = GameState[2][0]  #opponment's GameState goal
            #print('AI own goal in Max value : ', Own_goal,'Own goal GS', Own_goal_GS, 'Opp goal : ', Opp_goal, 'Opp goal GS ', Opp_goal_GS)
            for MAX_Index in range(6):
                #print('MAX_Index is:',MAX_Index)
                if MiniMax.originalSide[MAX_Index]  > 0:
                    print('marbles in original pit', MiniMax.originalSide[MAX_Index])
                    maxpayoff = (Own_goal-Own_goal_GS)-(Opp_goal-Opp_goal_GS)
                    MiniMax.maxPayofflist.append(maxpayoff)
                    MiniMax.maxpayoffindex.append(AI_Index)
                    #print('')
                    #print('the list of payoff is:  ',MiniMax.maxPayofflist)
                    #print('index of chosen pit:    ', MiniMax.maxpayoffindex)
                    choosehighest = MiniMax.maxPayofflist.index(max(MiniMax.maxPayofflist))
                    choosehighestindex = MiniMax.maxpayoffindex[choosehighest]
                    #print('choose highest value: ', choosehighest, 'The index to choose is: ',choosehighestindex)
                    MiniMax.indexToChoose = choosehighestindex
            playerVar = 'AI'
        elif state[4] == 'P':
            side_pits = state[1]
            Own_goal = state[2][0]
            Own_goal_GS = GameState[2][0]
            Opp_goal = state[3][0]  #opponment's goal
            Opp_goal_GS = GameState[3][0]  #opponment's GameState goal
            #print('p own goal : ', Own_goal,'Own goal GS', Own_goal_GS)
            playerVar = 'P'
        ChildGames_max = []
        heuristicValues = [0]*6
        #if MiniMax.terminalTest(state) or depth == depthlimit:                                                                  # function checkts if someone has won in previous step
        [terminal, state] = MiniMax().terminalTest(state)
        depth += 1
        if terminal: # or depth == depthlimit:
            heuristicValue = -100									                                # returns positiv value bc max player can finish the game
        elif depth >= depthlimit:
            # huerastic function: (new marbles in own kalaha) - (new marbles in player's kalaha)
            heuristicValue = (Opp_goal - Opp_goal_GS) - (Own_goal - Own_goal_GS)
            #print('heuristicValue in max is:', heuristicValue)
        else:
            for MAX_Index in range(6):
                #print('MAX_Index is:',MAX_Index)
                if side_pits[MAX_Index]  == 0:
                    ChildGames_max.append(state)
                    if playerVar == 'P':
                        heuristicValues[MAX_Index] = -1
                    if playerVar == 'AI':
                        heuristicValues[MAX_Index] = -1
                elif side_pits[MAX_Index]  > 0:                                                # for all northern pits with marbles
                    ChildGames_max.append(AIgame.AIgame().genChildGames(state,MAX_Index))			                # array with states for each index
                    #print('depht in maxvalue',depth)
                    MAX_state = ChildGames_max[MAX_Index]
                    while MAX_state[4] == playerVar:                                                         # while AI gets to go again, start new minimax iteration
                        #minimax = MiniMax.MiniMax()
                        depthlimitInWhile = 0
                        MAX_state = MiniMax().MINIMAX(MAX_state, depthlimitInWhile)[1]                                              # save new_MINMAX-nextGameState as 'state' to continue original MINMAX
                    heuristicValues[MAX_Index] = MiniMax().minValue(GameState, MAX_state, depth, depthlimit, AI_Index)				        # array with payoff for each index
                    #print('heuristicValues in max function:', heuristicValues)
            #end for
            heuristicValue = max(heuristicValues) #gets only updated after 'else' part is ealuated
        #end if
            #print('heuristic value is:', heuristicValue)
        return heuristicValue


    def terminalTest(self, state):
        # check if someone has won
        # state = [North_side,South_side,Vest_goal,East_goal,player]
        East_goal = state[3][0]
        Vest_goal = state[2][0]
        North_side = state[0]
        South_side = state[1]
        if East_goal > 36 or Vest_goal > 36 or Vest_goal+Vest_goal == 72:
            #if someone has more than half of all marbles in goal, or all marbles are gone
            state[4] = 'none'
            return [bool(True), state]
        if North_side == [0,0,0,0,0,0] or South_side == [0,0,0,0,0,0]:
            # if somene has no marbles left to play
            state[4] = 'none'
            return [bool(True), state]
        else:
            # game is not finished
            return [bool(False), state]


