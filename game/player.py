<<<<<<< HEAD
=======
import random, os
import time
import sys

def print_1(text):
    #this types out the words on the screen all fancy game-like. So instead of typing "print" type "print_1" and it should work for whatever statements are made!
    words = text
    time.sleep(.8)
    for char in words:
        time.sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('')
    
>>>>>>> ff3c3e691da145085b5512f2846e8fb28b4d545d
from hilo import Hilo

class Player:
    def __init__(self) -> None:
        """ 
<<<<<<< HEAD
=======
        Construct a player
>>>>>>> ff3c3e691da145085b5512f2846e8fb28b4d545d
        Construct a player object.
        """
        c = Hilo()
        self.cards = random.randint(1,14)
        self.points = 300
        self.is_playing = True
<<<<<<< HEAD
        self.total_points = 0
        self.hl = 0

    
=======
        self.total_points = ()
        self.card1 = random.randint(1,14)
        self.card2 = random.randint(1,14)
        
>>>>>>> ff3c3e691da145085b5512f2846e8fb28b4d545d
    def play_game(self):
        """
        Start the game Hilo 
        """
        while self.is_playing:
            card = Hilo()
<<<<<<< HEAD
            card.show_card1() 
            self.hl = card.high_or_low()                       
            self.update_points()
            card.show_card2()                                   
            self.display_score()
            self.play_again()
        

    def guess_hilo(self):
        """ 
        Ask user for a higher or lower guess. 
        """
        print_1("Higher or lower?")
        guess = input("[h/l]: ").lower()
        while guess != 'y' and guess != 'n':
            print_1("Sorry, please pick one of the given options.")
            guess = input("[h/l]: ").lower()
        return guess

    def update_points(self):
        """
        It will add or substract point from the user. 
        """
        player_guess = self.guess_hilo()

        if (self.hl == 1 and player_guess == "h") or (self.hl == 0 and player_guess == "l"):
            self.points += 100
        elif (self.hl == 1 and player_guess == "l") or (self.hl == 0 and player_guess == "h"):
            self.points -= 75
        else:
            self.points += 0
    
=======
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
        # guess = input("Higher or lower? [h/l] ")
        # return guess

    def update_points(self):
        """
        It will add or substract point from the user. 
        """
        guess = input("Higher or lower? [h/l] ")
        if guess == "h" and self.card2 > self.card1:
            self.points += 100
        if guess == "h" and self.card2 < self.card1:
            self.points -= 75
        if guess == "l" and self.card2 < self.card1:
            self.points += 100  
        if guess == "l" and self.card2 > self.card1:
            self.points -= 75
        # if (guess == 1 and self.guess_hilo == "h") or (guess == -1 and self.guess_hilo == "l"):
        #     self.points += 100
        # elif (guess == 1 and self.guess_hilo == "l") or (guess == -1 and self.guess_hilo == "h"):
        #     self.points -= 75
        
>>>>>>> ff3c3e691da145085b5512f2846e8fb28b4d545d
    def display_score(self):
        """
        Display final score to the player.
        """
<<<<<<< HEAD
        self.total_points = self.points
        print(f'Your score is:  {self.total_points}')

    def play_again(self):
        """
        Ask the user if they want to play again and check if points are not 0
        """
        print_1("Play again?")
        again = input("[y/n]: ").lower()
        while again != "y" and again != "n":
                print_1("Sorry, please pick one of the given options.")
                again = input("[y/n]: ").lower()
        if self.points > 0 and again == "y":
            self.is_playing = True
            print()
        elif self.points <= 0 or again == "n":
            print("Game is over.")
            print()
            self.is_playing = False 
            print_1("Press 'enter' to exit")
            input(" ")
            exit()
            

#p = Player()
#p.play_game() 


=======
        self.total_points = self.points 
        print(f'Your score is:  {self.total_points}')
>>>>>>> ff3c3e691da145085b5512f2846e8fb28b4d545d

    def play_again(self):
        """
        Ask the user if they want to play again and check if points are not 0
        """
        print_1("Play again?")
        again = input("[y/n]: ").lower()
        while again != "y" and again != "n":
                print_1("Sorry, please pick one of the given options.")
                again = input("[y/n]: ").lower()
        if self.points > 0 and again == "y":
            self.is_playing = True
        elif self.points <= 0 or again == "n":
            print_1("Game Over")
            print_1(f"Total score: {self.total_points}")
            self.is_playing = False
            print()
        print_1("Press 'enter' to exit")
        input(" ")
        exit()
        
        
