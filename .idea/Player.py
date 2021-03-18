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
        move = input("Choose a pit from your side and type index number")
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
            Play1.Move()
            print('P gets to moe again player is: ', Player.player)
        elif Game1.Game1.Last_Pit[0]=='AI' and Game1.Game1.Last_Pit[1]=='AIg':
            Player.player = 'AI'
            Play1.Move()
            print("AI gets to move again", Player.player)
        elif Game1.Game1.Last_Pit[0]=='P' and Game1.Game1.Last_Pit[1]=='n':
            Player.player= 'AI'
            Play1.Move()
            print("Tha player changes fromP to AI ", Player.player)
        elif Game1.Game1.Last_Pit[0]=='AI' and Game1.Game1.Last_Pit[1]=='s':
            Player.player= 'P'
            print("The player changes from AI to P", Player.player)
            Play1.Move()
        



Play = Player()
Play.BeginPlay()
Play.Turn()
