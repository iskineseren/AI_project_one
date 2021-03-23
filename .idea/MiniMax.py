#import Player
import Game1

class MiniMax:

    AInorthside = Game1.Game1.North_side
    #AIgoal = [0, 1, 0, 2, 3, 4]
    AIgoal = Game1.Game1.East_goal
    Playersouthside = Game1.Game1.South_side
    Playergoal = Game1.Game1.Vest_goal
    indexwithgreatestpayoff = 0

    # Get boardstate
    def BestMove():
        try:
            for x in MiniMax.AInorthside:
                AIgoalmax = max(MiniMax.AIgoal) #maximum-værdi af Eastgoal
                print("Max value of AIgoal: ", AIgoalmax)
                indexwithgreatestpayoff = Minimax.AIgoal.index(AIgoalmax) #indeks-nr for eastgoals max-værdi
                print("Index-nr.: ", indexwithgreatestpayoff)

                return indexwithgreatestpayoff


        except Exception as e:
            print("Exception caught: ", e)


    def Move(self):
        move = MiniMax.indexwithgreatestpayoff
        Kalaha = Game1.Game1()
        Kalaha.UpdateBoard('AI', move)
        Kalaha.Board()
        print("updated board ")



    def MINIMAX(GameState):
        # returns index of Pit that AI whoud use for the next move
        depthlimit = 5                                                                              # mimimaxfunction iterates max step
        ChildGames      = [0]*6
        heuristicValues = [0]*6
        for AI_Index in range(6):
            if Gamestate.North_side[AI_Index]  > 0:                                                 # for all northern pits with marbles
                ChildGames[AI_Index] = ChildGames.append(genChildGames(GameState, AI_Index)) 		# list with states for each index
                depth = 1
                state = ChildGames[AI_Index]
                heuristicValues[AI_Index] = minValue(GameState, state ,depth)		                # array with payoff for each index
                    # GameState = actual current state in game
                    # state = ChildGames(AI_Index), calculated belief state
            #end if
        #end for
        # returns index of max payoff -> same than best pit_index to choose from
        indexwithgreatestpayoff = heuristicValues.index(max(heuristicValues))
        return indexwithgreatestpayoff

    def minValue(GameState, state, depth):
        # returns a utility / heurastic value
        if TERMINAL-TEST(state):               # still MISSING !!                                   # function checkts if someone has won in previous step
            heuristicValue = 100									                                # returns positiv value bc max player can finish the game
        elif depth == depthlimit:
            # huerastic function: (new marbles in own kalaha) - (new marbles in player's kalaha)
            heuristicValue = (state.east_goal - GameState.east_goal) - (state.vest_goal - GameState.vest_goal)
        else:
            for MIN_Index in range(6):
                if state.North_side[MIN_Index]  > 0:
                # for all northern pits with marbles
                ChildGames_min(MIN_Index) = genChildGames(state,MIN_Index) 			                # array with states for each index
                depth += 1
                MIN_state = ChildGames_min[MIN_Index]
                heuristicValues(MIN_Index) = maxValue(GameState, MIN_state, depth)				        # array with payoff for each index
            #end for
            heuristicValue = min(heurasticValues) #gets only updated after 'else' part is ealuated
        #end if
        return heuristicValue


        def maxValue(GameState, state, depth):
        # returns a utility / heurastic value
        if TERMINAL-TEST(state):               # still MISSING !!                                   # function checkts if someone has won in previous step
            heuristicValue = -100									                                # returns positiv value bc max player can finish the game
        elif depth == depthlimit:
            # huerastic function: (new marbles in own kalaha) - (new marbles in player's kalaha)
            heuristicValue = (state.east_goal - GameState.east_goal) - (state.vest_goal - GameState.vest_goal)
        else:
            for MAX_Index in range(6):
                if state.North_side[MAX_Index]  > 0:                                                # for all northern pits with marbles
                    ChildGames_max(MAX_Index) = genChildGames(state,MAX_Index) 			                # array with states for each index
                    depth += 1
                    MAX_state = ChildGames_max[MAX_Index]
                    heuristicValues(MAX_Index) = minValue(GameState, MAX_state, depth)				        # array with payoff for each index
            #end for
            heuristicValue = max(heurasticValues) #gets only updated after 'else' part is ealuated
        #end if
        return heuristicValue


    def TERMINAl_TEST(state):
        # check if someone has won

MiniMax = MiniMax()
MiniMax.BestMove()
print(indexwithgreatestpayoff)

