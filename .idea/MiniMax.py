#import Player
import AIGame

class MiniMax:
    player = None
    # Last_Pit = Game1.Game1.Last_Pit
    continueGame= True
    AInorthside = AIGame.AIGame.North_side
    AIsouthside = AIGame.AIGame.South_side
    #AIgoal = [0, 1, 0, 2, 3, 4]
    AIgoal = AIGame.AIGame.East_goal
    Playersouthside = AIGame.AIGame.South_side
    Playergoal = AIGame.AIGame.Vest_goal
    pit_to_choose = 0

    # Get boardstate
    def maxCheck(self):
            #  for x in MiniMax.AInorthside:
        i=0
        while i<6:
            #print(MiniMax.AInorthside)
            marbles = MiniMax.AInorthside[i]
            if marbles == (6-i):
                print('This is the index to choose', i)
                MiniMax.pit_to_choose = i
            elif marbles == 13 and MiniMax.AIsouthside[i] > 1:
                MiniMax.pit_to_choose = i
                print('This is the index to choose instead', i)
            i+=1






