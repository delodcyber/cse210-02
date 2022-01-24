import hilo

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
        Construct a player
        """
        self.points = 300
        self.guess = ""
        self.is_playing = True
        self.total_points = 0

    def play_game(self):
        """
        Start the game Hilo 
        """
        while self.is_playing:
            pass
    def guess_hilo(self):
        """
        Ask user for a higher or lower guess. 
        """
        guess = input("Higher or lower? [h/l] ")

        