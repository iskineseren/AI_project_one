import Game
class Player:
    player = None

    def BeginPlay(self): # This methods begins the play
        Kalaha = Game.Game()
        Kalaha.Board()

        startplayer = input("Would you like to begin? (Y/N)")
        if (startplayer.lower() == 'y'):
            print("You begin!")
            Player.player = 'P'
            Play1 = Player()
            Play1.Move()
            print(Player.player)
        elif (startplayer.lower() == 'n'):
            print("Computer begins")
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
        Kalaha = Game.Game()
        Kalaha.UpdateBoard(Player.player, move)
        Kalaha.Board()
        print("updated board ")


    def Turn(player):
        print("This is the chosen player: " + player)



Play = Player()
Play.BeginPlay()
