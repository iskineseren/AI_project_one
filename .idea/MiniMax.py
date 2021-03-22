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


MiniMax = MiniMax()
MiniMax.BestMove()
print(indexwithgreatestpayoff)

