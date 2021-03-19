import Game1
class Player:
    player = None
    Last_Pit = Game1.Game1.Last_Pit

    def BeginPlay(self): # This methods begins the play
        Kalaha = Game1.Game1()
        Kalaha.Board()

        startplayer = input('Would you like to begin? (Y/N)')
        if (startplayer.lower() == 'y'):
            print('You begin!')
            Player.player = 'P'
            Play1 = Player()
            Play1.Move()
            print(Player.player)
        elif (startplayer.lower() == 'n'):
            print('Computer begins')
            Player.player = 'AI'
            Play2 = Player()
            Play2.Move()
            print(Player.player)
        else:
            print('Wrong input')
            Play = Player()
            Play.WhoBegins()




    def Move(self):
        print('It is player ',Player.player,)
        move = input('Choose a pit from your side and type index number')
        move = int(move)
        Kalaha = Game1.Game1()
        Kalaha.UpdateBoard(Player.player, move)
        Kalaha.Board()
        print("updated board ")
        print('The player is: ',Player.player, 'Move is: ', move)

    def Turn(self):
        #Game1.Game1.Last_Pit
        while True:
            Play1 = Player()
            if Game1.Game1.Last_Pit[0]=='P' and Game1.Game1.Last_Pit[1]=='g':
                Player.player = 'P'
                print('P gets to move again player is: ', Player.player)
                Play1.Move()

            elif Game1.Game1.Last_Pit[0]=='AI' and Game1.Game1.Last_Pit[1]=='AIg':
                Player.player = 'AI'
                Play1.Move()
                print("AI gets to move again", Player.player)

            elif Game1.Game1.Last_Pit[0]=='P' and Game1.Game1.Last_Pit[1]=='n':
                print("The player is", Player.player)
                Player.player= 'AI'
                print("Tha player changes from P to ", Player.player)
                Play1.Move()

            elif Game1.Game1.Last_Pit[0]=='AI' and Game1.Game1.Last_Pit[1]=='s':
                print("The player is", Player.player)
                Player.player= 'P'
                print("The player changes to", Player.player)
                Play1.Move()

            elif Game1.Game1.Last_Pit[0]=='P' and Game1.Game1.Last_Pit[1]=='s'and Game.Game.Last_Pit[3]!=1:
                print("The player is", Player.player)
                Player.player= 'AI'
                print("Tha player changes from P to ", Player.player)
                Play1.Move()

            elif Game1.Game1.Last_Pit[0]=='AI' and Game1.Game1.Last_Pit[1]=='n'and Game1.Game1.Last_Pit[3]!=1:
                print("The player is", Player.player)
                Player.player= 'P'
                print("Tha player changes from AI to ", Player.player)
                Play1.Move()



Play = Player()
Play.BeginPlay()
Play.Turn()

