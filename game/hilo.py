import sys
import time
def print_1(text):
    #this types out the words on the screen all fancy game-like. So instead of typing "print" type "print_1" and it should work for whatever statements are made!
    words = text
    time.sleep(.8)
    for char in words:
        time.sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('')

print_1(">Welcome to HiLo Games<")
import random

class Hilo:
    """
    Individual cards are represented as a number from 1 to 13. 
    Current card will be displayed. 
    The next card will be displayed. 
    """

    def __init__(self) -> None:
        """
        Initialize two random cards.
        """
<<<<<<< HEAD
        self.card1 = random.randint(1,13)
        self.card2= random.randint(1,13)
    
=======
        self.card1 = random.randint(1,14)
        self.card2 = random.randint(1,14)

>>>>>>> ff3c3e691da145085b5512f2846e8fb28b4d545d
    def show_card1(self):
        """
        Display first card to the user.
        """
        output = f'The card is: {self.card1}'
        print_1(output)

    def show_card2(self):
        """
        Display second card to the user. 
        """
<<<<<<< HEAD
        output = f'The card is: {self.card2}'
        print_1(output)

    
=======
        output = f'Next card was: {self.card2}'
        print_1(output)


>>>>>>> ff3c3e691da145085b5512f2846e8fb28b4d545d
    def high_or_low(self):
        """
        Check high card or low card. 
        """
        if self.card2 > self.card1:     # check for high card
            return 1
        elif self.card2 < self.card1:   # check for low card
<<<<<<< HEAD
            return 0
        else:                           # same value card
            return -1
=======
            return -1 
        
>>>>>>> ff3c3e691da145085b5512f2846e8fb28b4d545d
