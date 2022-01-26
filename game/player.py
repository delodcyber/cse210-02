import random
from hilo import Hilo

class Player:
    def __init__(self) -> None:
        """ 
        Construct a player
        Construct a player object.
        """
        c = Hilo()
        self.points = 300
        self.is_playing = True
        self.total_points = 0
        self.card1 = random.randint(1,14)
        self.card2 = random.randint(1,14)
        
    def play_game(self):
        """
        Start the game Hilo 
        """
        while self.is_playing:
            card = Hilo()
            car1 = card.show_card1()
            self.guess_hilo()
            self.update_points()
            car2 = card.show_card2()
            self.display_score()
            self.play_again()

    def guess_hilo(self):
        """
        #Ask user for a higher or lower guess. 
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
            # while True:
            #     choice = input("higher or lower? [h/l] ")
            #     if len(choice) > 0:
            #         if choice[0].lower() in ["h","l"]:
            #             break
                # if (self.guess_hilo == 1 and self.card2 > self.card1):
                #     self.points += 100
                # elif (self.guess_hilo == -1 and self.card2 < self.card1):
                #     self.points -= 75
                # elif (self.guess_hilo == 1 and self.card2 < self.card1):
                #     self.points += 100
                # elif (self.guess_hilo == -1 and self.card2 > self.card1):
                #     self.points -= 75
                #else:
                #    print("Draw!")

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
            print("Game Over")
            print(f"Total score: {self.total_points}")
            self.is_playing = False
        print()