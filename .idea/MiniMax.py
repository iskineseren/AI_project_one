#import Player
import Game1
import AIgame
class MiniMax:

#    AInorthside = Game1.Game1.side_pits
#    #AIgoal = [0, 1, 0, 2, 3, 4]
#    AIgoal = Game1.Game1.East_goal
#    Playersouthside = Game1.Game1.South_side
#    Playergoal = Game1.Game1.Vest_goal
#    indexwithgreatestpayoff = 0
#
#    # Get boardstate
#    def BestMove():
#        try:
#            for x in MiniMax.AInorthside:
#                AIgoalmax = max(MiniMax.AIgoal) #maximum-værdi af Eastgoal
#                print("Max value of AIgoal: ", AIgoalmax)
#                indexwithgreatestpayoff = Minimax.AIgoal.index(AIgoalmax) #indeks-nr for eastgoals max-værdi
#                print("Index-nr.: ", indexwithgreatestpayoff)
#
#                return indexwithgreatestpayoff
#
#
#        except Exception as e:
#            print("Exception caught: ", e)
    def getInitialstate(self):
    #This is the same as Gamestate in MiniMax
        North_side = Game1.Game1.North_side
        South_side = Game1.Game1.South_side
        Vest_goal = Game1.Game1.Vest_goal
        East_goal  = Game1.Game1.East_goal
        player = 'AI'
        GameState = [North_side,South_side,Vest_goal,East_goal,player]
        return GameState

    # def Move(self):
    #     move = MiniMax.indexwithgreatestpayoff
    #     Kalaha = Game1.Game1()
    #     Kalaha.UpdateBoard('AI', move)
    #     Kalaha.Board()
    #     print("updated board ")


    def MINIMAX(self, GameState, depthlimit):
        #GameState = [side_pits,South_side,Vest_goal,East_goal,player]
        # returns index of Pit that AI whoud use for the next move and the next state that gets created by choosing the pit
        print('')
        print('')
        print('*** MINIMAX FUNCTION START')
        print('inside minimax: state', GameState)
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
        #while True:
            #if GameState[4] == 'none':
                #return False
        for AI_Index in range(6):
                print('AI_Index is:',AI_Index)
                if side_pits[AI_Index]  == 0:
                    ChildGames.append(GameState)
                elif side_pits[AI_Index]  > 0:                                                 # for all northern pits with marbles
                    print('north side in minimax',side_pits[AI_Index])
                    ch = ai.genChildGames(GameState, AI_Index)
                    #print('child',ch)
                    ChildGames.append(ch) 		# list with states for each index
                    print('child received from genchild',ChildGames)
                    print('AI_Index is ',AI_Index)
                    depth = 0
                    state = ChildGames[AI_Index]                                                 # [0] bc it returns a list inide of a list
                    print('returned state in Minimax',state, 'player is', state[4])
                    while state[4] == playerVar:                                                         # while AI gets to go again, start new minimax iteration
                        #minimax = MiniMax.MiniMax()
                        depthlimitInWhile = 0
                        state = MiniMax().MINIMAX(state, depthlimitInWhile)[1]
                    heuristicValues[AI_Index] = MiniMax().minValue(GameState, state ,depth, depthlimit)		                # array with payoff for each index
                    print('heuristicValues in minimax function:', heuristicValues)
                    print('depht is:', depth)
                    # GameState = actual current state in game
                    # state = ChildGames(AI_Index), calculated belief state
                #end if
            #end for
        # returns index of max payoff -> same than best pit_index to choose from

        indexwithgreatestpayoff = heuristicValues.index(max(heuristicValues))
        nextGameState = ChildGames[heuristicValues.index(max(heuristicValues))]
        print('MINIMAX FUNCTION DONE')
        print('Print in minimax: ',indexwithgreatestpayoff, nextGameState)
        return [indexwithgreatestpayoff, nextGameState]

    def minValue(self, GameState, state, depth, depthlimit):
        print('')
        print('')
        print('*** MIN-VALUE FUNCTION START')
        # returns a utility / heuristic value
        # state = [North_side,South_side,Vest_goal,East_goal,player]
        if state[4] == 'AI':
            side_pits = state[0]
            Own_goal = state[3][0]
            Own_goal_GS = GameState[3][0]
            Opp_goal = state[2][0]  #opponment's goal
            Opp_goal_GS = GameState[2][0]  #opponment's GameState goal
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
            print('heuristicValue in min is:', heuristicValue)
        else:
            for MIN_Index in range(6):
                print('MIN_Index is:',MIN_Index)
                if side_pits[MIN_Index]  == 0:
                    ChildGames_min.append(state)
                elif side_pits[MIN_Index]  > 0:
                # for all northern pits with marbles
                    ChildGames_min.append(AIgame.AIgame().genChildGames(state,MIN_Index)) 			                # array with states for each index
                    print('depth in minvalue:', depth)
                    MIN_state = ChildGames_min[MIN_Index]
                    while MIN_state[4] == playerVar:                                          # while Player gets to go again, start new minimax iteration (in this recursion player is max, AI is min)
                        #minimax = MiniMax.MiniMax()
                        depthlimitInWhile = 0
                        MIN_state = MiniMax().MINIMAX(MIN_state, depthlimitInWhile)[1]
                        print('state minstate', MIN_state)# save new_MINMAX-nextGameState as 'state' to continue original MINMAX
                    heuristicValues[MIN_Index] = MiniMax().maxValue(GameState, MIN_state, depth, depthlimit)				        # array with payoff for each index
                    print('heuristicValues in min function:', heuristicValues)
            #end for
            heuristicValue = min(heuristicValues) #gets only updated after 'else' part is ealuated
        #end if
        return heuristicValue


    def maxValue(self, GameState, state, depth, depthlimit):
        print('*** MAX VALUE FUNCTION START')
        print('')
        print('')
        # returns a utility / heuristic value
        # state = [North_side,South_side,Vest_goal,East_goal,player]
        if state[4] == 'AI':
            side_pits = state[0]
            Own_goal = state[3][0]
            Own_goal_GS = GameState[3][0]
            Opp_goal = state[2][0]  #opponment's goal
            Opp_goal_GS = GameState[2][0]  #opponment's GameState goal
            playerVar = 'AI'
        elif state[4] == 'P':
            side_pits = state[1]
            Own_goal = state[2][0]
            Own_goal_GS = GameState[2][0]
            Opp_goal = state[3][0]  #opponment's goal
            Opp_goal_GS = GameState[3][0]  #opponment's GameState goal
            playerVar = 'P'
        ChildGames_max = []
        heuristicValues = [0]*6
        #if MiniMax.terminalTest(state) or depth == depthlimit:                                                                  # function checkts if someone has won in previous step
        [terminal, state] = MiniMax().terminalTest(state)
        depth += 1
        if terminal: # or depth == depthlimit:
            heuristicValue = -100									                                # returns positiv value bc max player can finish the game
        elif depth == depthlimit:
            # huerastic function: (new marbles in own kalaha) - (new marbles in player's kalaha)
            heuristicValue = (Opp_goal - Opp_goal_GS) - (Own_goal - Own_goal_GS)
            print('heuristicValue in max is:', heuristicValue)
            print(' ')
        else:
            for MAX_Index in range(6):
                print('MAX_Index is:',MAX_Index)
                if side_pits[MAX_Index]  == 0:
                    ChildGames_max.append(state)
                elif side_pits[MAX_Index]  > 0:                                                # for all northern pits with marbles
                    ChildGames_max.append(AIgame.AIgame().genChildGames(state,MAX_Index))			                # array with states for each index
                    print('depht in maxvalue',depth)
                    MAX_state = ChildGames_max[MAX_Index]
                    while MAX_state[4] == playerVar:                                                         # while AI gets to go again, start new minimax iteration
                        #minimax = MiniMax.MiniMax()
                        depthlimitInWhile = 0
                        MAX_state = MiniMax().MINIMAX(MAX_state, depthlimitInWhile)[1]                                              # save new_MINMAX-nextGameState as 'state' to continue original MINMAX
                    heuristicValues[MAX_Index] = MiniMax().minValue(GameState, MAX_state, depth, depthlimit)				        # array with payoff for each index
                    print('heuristicValues in max function:', heuristicValues)
            #end for
            heuristicValue = max(heuristicValues) #gets only updated after 'else' part is ealuated
        #end if
            print('heuristic value is:', heuristicValue)
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


