#import Player
import Game1
import AIgame
class MiniMax:

#    AInorthside = Game1.Game1.North_side
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

    def Move(self):
        move = MiniMax.indexwithgreatestpayoff
        Kalaha = Game1.Game1()
        Kalaha.UpdateBoard('AI', move)
        Kalaha.Board()
        print("updated board ")


    def MINIMAX(self,GameState):
        #GameState = [North_side,South_side,Vest_goal,East_goal,player]
        # returns index of Pit that AI whoud use for the next move and the next state that gets created by choosing the pit
        print('inside minimax: state', GameState)
        North_side = GameState[0]
        ai = AIgame.AIgame()
        depthlimit = 3                                                                              # mimimaxfunction iterates max step
        ChildGames      = []
        heuristicValues = [0]*6
        for AI_Index in range(6):
            if North_side[AI_Index]  > 0:                                                 # for all northern pits with marbles
                print('north side in minimax',North_side[AI_Index])
                ch = ai.genChildGames(GameState, AI_Index)
                #print('child',ch)
                ChildGames.append(ch) 		# list with states for each index
                print('child received from genchild',ChildGames)
                depth = 1
                state = ChildGames[AI_Index]                                                 # [0] bc it returns a list inide of a list
                print('returned state in Minimax',state, 'player is', state[4])
                while state[4] == 'AI':                                                         # while AI gets to go again, start new minimax iteration
                    minimax = MiniMax
                    [contiVari, state] = minimax.MINIMAX(state)                                             # save new_MINMAX-nextGameState as 'state' to continue original MINMAX
                    ## maybe it would make sense to set a different depth limit to the recursions -> depthlimit would need to be a input to MINMAX
                heuristicValues[AI_Index] = MiniMax.minValue(GameState, state ,depth, depthlimit)		                # array with payoff for each index
                    # GameState = actual current state in game
                    # state = ChildGames(AI_Index), calculated belief state
            #end if
        #end for
        # returns index of max payoff -> same than best pit_index to choose from
        indexwithgreatestpayoff = heuristicValues.index(max(heuristicValues))
        nextGameState = ChildGames[heuristicValues.index(max(heuristicValues))]
        return [indexwithgreatestpayoff, nextGameState]

    def minValue(self, GameState, state, depth, depthlimit):
        # returns a utility / heurastic value
        # state = [North_side,South_side,Vest_goal,East_goal,player]
        East_goal = state[3][0]
        Vest_goal = state[2][0]
        North_side = state[0]
        South_side = state[1]
        ChildGames_min = []
        heuristicValues = [0]*6
        if MiniMax.terminalTest(state):                                                                    # function checkts if someone has won in previous step
            heuristicValue = 100									                                # returns positiv value bc max player can finish the game
        elif depth == depthlimit:
            # huerastic function: (new marbles in own kalaha) - (new marbles in player's kalaha)
            heuristicValue = (East_goal - GameState[3][0]) - (Vest_goal - GameState[2][0])
        else:
            for MIN_Index in range(6):
                if South_side[MIN_Index]  > 0:
                # for all northern pits with marbles
                    ChildGames_min.append(AIgame.AIgame().genChildGames(state,MIN_Index)) 			                # array with states for each index
                    depth += 1
                    MIN_state = ChildGames_min[MIN_Index]
                    while MIN_state[4] == 'P':                                                     # while Player gets to go again, start new minimax iteration (in this recursion player is max, AI is min)
                        [contiVari, MIN_state] = MINIMAX(MIN_state)                                         # save new_MINMAX-nextGameState as 'state' to continue original MINMAX
                    heuristicValues[MIN_Index] = MiniMax.maxValue(GameState, MIN_state, depth, depthlimit)				        # array with payoff for each index
            #end for
            heuristicValue = min(heurasticValues) #gets only updated after 'else' part is ealuated
        #end if
        return heuristicValue


    def maxValue(self, GameState, state, depth, depthlimit):
        # returns a utility / heurastic value
        East_goal = state[3][0]
        Vest_goal = state[2][0]
        North_side = state[0]
        South_side = state[1]
        ChildGames_max = []
        heuristicValues = [0]*6
        if MiniMax.terminalTest(state):                                                                   # function checkts if someone has won in previous step
            heuristicValue = -100									                                # returns positiv value bc max player can finish the game
        elif depth == depthlimit:
            # huerastic function: (new marbles in own kalaha) - (new marbles in player's kalaha)
            heuristicValue = (East_goal - GameState[3][0]) - (Vest_goal - GameState[2][0])
        else:
            for MAX_Index in range(6):
                if North_side[MAX_Index]  > 0:                                                # for all northern pits with marbles
                    ChildGames_max.append(AIgame.AIgame().genChildGames(state,MAX_Index))			                # array with states for each index
                    depth += 1
                    MAX_state = ChildGames_max[MAX_Index][0]
                    while MAX_state[4] == 'AI':                                                         # while AI gets to go again, start new minimax iteration
                        [contiTurn, MAX_state] = MINIMAX(MAX_state)                                             # save new_MINMAX-nextGameState as 'state' to continue original MINMAX
                    heuristicValues[MAX_Index] = MiniMax.minValue(GameState, MAX_state, depth, depthlimit)				        # array with payoff for each index
            #end for
            heuristicValue = max(heurasticValues) #gets only updated after 'else' part is ealuated
        #end if
        return heuristicValue


    def terminalTest(self, state):
        # check if someone has won
        # state = [North_side,South_side,Vest_goal,East_goal,player]
        East_goal = state[3][0]
        Vest_goal = state[2][0]
        North_side = state[0]
        South_side = state[1]
        if East_goal > 36 or Vest_goal > 36 or Vest_goal+Vest_goal == 72:
            # if someone has more than half of all marbles in goal, or all marbles are gone
            return bool(True)
        elif North_side == [0,0,0,0,0,0] or South_side == [0,0,0,0,0,0]:
            # if somene has no marbles left to play
            return bool(True)
        else:
            # game is not finished
            return bool(False)



MiniMax = MiniMax()
m = MiniMax.getInitialstate()
MiniMax.MINIMAX(m)
# print(indexwithgreatestpayoff)

