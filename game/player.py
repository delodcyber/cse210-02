from hilo import Hilo

class Player:
    """
    The player direct control the game. 
    Player starts the game with 300 points.
    If player guess higher or lower:
    - The player earns 100 points if guess is correct.
    - The player loses 75 points if they guessed is incorrectly. 
    - If player reaches 0 points the game is over. 
    Player decides to keep playing or stop the game. 
    """
    def __init__(self) -> None:
        """ 
        Construct a player object.
        """
        self.points = 300
        #self.guess = ""
        self.is_playing = True
        self.total_points = 0
        c = Hilo()

    def play_game(self):
        """
        Start the game Hilo 
        """
        while self.is_playing:
            Hilo.show_card1(self)
            self.guess_hilo()
            self.update_points()
            Hilo.show_card2(self)
            self.display_score()
            self.play_again()
        

    def guess_hilo(self):
        """ 
        Ask user for a higher or lower guess. 
        """
        guess = input("Higher or lower? [h/l] ")
        return guess

    def update_points(self):
        """
        It will add or substract point from the user. 
        """
        if (Hilo.high_or_low == 1 and self.guess_hilo == "h") or (Hilo.high_or_low == -1 and self.guess_hilo == "l"):
            self.points += 100
        elif (Hilo.high_or_low == 1 and self.guess_hilo == "l") or (Hilo.high_or_low == -1 and self.guess_hilo == "h"):
            self.points -= 75
    
    def display_score(self):
        """
        Display final score to the player.
        """
        self.total_points = self.points
        print(f'Your score is:  {self.total_points}')

    def play_again(self):
        """
        Ask the user if they want to play again and check if points are not 0
        """
        again = input("Play again? [y/n] ")
        if self.points > 0 and again == "y":
            self.is_playing = True
        elif self.points <= 0 or again == "n":
            print("Game is over.")
            self.is_playing = False

p = Player()
p.play_game()



        