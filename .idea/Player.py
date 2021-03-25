import Game1
class Player:
    player = None
    Last_Pit = Game1.Game1.Last_Pit
    continueGame= True

    def BeginPlay(self): # This methods begins the play
        Kalaha = Game1.Game1()
        Kalaha.Board()
        Play1 = Player()
        startplayer = input('Would you like to begin? (Y/N)')
        if (startplayer.lower() == 'y'):
            print('You begin!')
            Player.player = 'P'
            #Play1 = Player()
            Play1.Move()
            #print(Player.player)
        elif (startplayer.lower() == 'n'):
            print('Computer begins')
            Player.player = 'AI'
            #Play2 = Player()
            Play1.Move()
           # print(Player.player)
        else:
            print('Wrong input')
            #Play = Player()
            Play1.BeginPlay()




    def Move(self):
        #print('It is player ',Player.player,)
        if Player.player =='P':
            move = input('Choose a pit from your side and type index number')
            move = int(move)
        elif Player.player =='AI':
            M=MiniMax.MiniMax()
            move = M.maxCheck()
            move = MiniMax.MiniMax.pit_to_choose
            move = (move+1)

        x = [1,2,3,4,5,6]
        if move not in x:
            print('You have to choose a pit from 1 to 6')
            Play3 = Player()
            Play3.Move()
        elif (Player.player=='P' and Game1.Game1.South_side[move - 1] == 0) or(Player.player=='AI' and Game1.Game1.North_side[move - 1] == 0):
            print('No marbles to take! Please select another pit.')
            Play4 = Player()
            Play4.Move()
        else:
            Kalaha = Game1.Game1()
            Kalaha.UpdateBoard(Player.player, move)
            Kalaha.Board()
            #print("updated board ")
            #print('The player is: ',Player.player, 'Move is: ', move)

    def Turn(self):
        #print('Status of Northside', Game1.Game1.North_side_status,'Status of South side', Game1.Game1.South_side_status)
        Play1 = Player()
        #print(Player.continueGame)
        Play.checkWinner()
        #print(Player.continueGame)
        while Player.continueGame:
            if Game1.Game1.Last_Pit[0]=='P' and Game1.Game1.Last_Pit[1]=='g':
                Player.player = 'P'
                print('You get to move again!') #player is: ', Player.player
                Play1.Move()

            elif Game1.Game1.Last_Pit[0]=='AI' and Game1.Game1.Last_Pit[1]=='AIg':
                Player.player = 'AI'
                print("Computer gets to move again")
                Play1.Move()

            elif Game1.Game1.Last_Pit[0]=='P': #and Game1.Game1.Last_Pit[1]=='n':
                #print("The player is", Player.player)
                Player.player= 'AI'
                print('Computer has the turn')
                #print("The player changes from you to ", Player.player)
                Play1.Move()

            elif Game1.Game1.Last_Pit[0]=='AI':# and Game1.Game1.Last_Pit[1]=='s':
                #print("The player is", Player.player)
                Player.player= 'P'
                print('Your turn!')
                #print("The player changes to", Player.player)
                Play1.Move()

    def checkWinner(self):
        x = Game1.Game1.East_goal[0]
        y = Game1.Game1.Vest_goal[0]
        #print('Eastgoal is',x, 'Vestgoal is:', y )
        if y > 36:
            print('You Win')
            Player.continueGame= False
        elif x > 36:
            print('Computer wins')
            Player.continueGame= False
        #else:
         #   print('Continue')




Play = Player()
Play.BeginPlay()
Play.Turn()

