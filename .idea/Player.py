import Game1
class Player:

    def WhoBegins(self): # This methods decide who begins based on user input
        startplayer = input("Would you like to play? (Y/N)")
        if (startplayer.lower() == 'y'):
            print("You begin. Choose a pit from your side and type index number")
            player = 'P'
        elif (startplayer.lower() == 'n'):
            print("Computer begins")
            player = 'AI'
            print(player)
        #Pl = Player()
        #Pl.Turn(player)


    def Turn(player):
        print("This is the chosen player: " + player)


Kalaha = Game1.Game1()
Kalaha.NewBoard()
Play = Player()
Play.WhoBegins()