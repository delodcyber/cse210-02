import time
import sys
import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#list of cards


def print_1(text):
    #this types out the words on the screen. so instead of typing "print" type "print_1" and it should work for whatever statements are made!
    words = text
    time.sleep(.8)
    for char in words:
        time.sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('')
def print_0(text):
    #same thing as above, but EVEN FASTER
    words = text
    time.sleep(.3)
    for char in words:
        time.sleep(0.02)
        sys.stdout.write(char)
        sys.stdout.flush()
    print('')

def intro():
    #This introduces the game and the rules of said game.
    print_1('Welcome to HILO!')
    print_1("Would you like to hear the rules of the game?")
    rules = input("Hear the rules? (YES/NO): ").lower()
    while rules != 'yes' and rules != 'no':
        print_1('Sorry, please pick one of the options.')
        play = input('Hear the rules? (YES/NO): ').lower()
        #while loops to make sure that the player doesn't accenentally type something weird and send the game flying into cardiac arrest
    if rules == 'yes':
        print()
        print_1('RULES:')
        print_0('--- The player starts the game with 300 points.')
        print_0('--- Individual cards are represented as a number from 1 to 13.')
        print_0('--- The current card is displayed.')
        print_0('--- The player guesses if the next one will be higher or lower.')
        print_0('--- Then the next card is displayed.')
        print_0('--- The player earns 100 points if they guessed correctly.')
        print_0('--- The player loses 75 points if they guessed incorrectly.')
        print_0('--- If a player reaches 0 points the game is over.')
        #IDK how I feel about how slowly it types out... should I cut out the type sequences?
        print()
    elif rules == 'no':
        print_1('Aright, I hope you remember them then')

    print_1('Would you like to play HILO?')
    play = input('Play? (YES/NO): ').lower()
    while play != 'yes' and play != 'no':
        print_1('Sorry, please pick one of the options.')
        play = input('Play? (YES/NO): ').lower()
    if play == 'yes':
        pass
    elif play == 'no':
        print_1('Alright, have a nice day then!')
        #How passive agressive do we want our game haha
        input("Press 'ENTER' to exit")
        exit()
    
def gamestart():
    random.choice(cards)
    #picks are random card... hopefully
    
    print(random.choice(cards))
    #this show us the card it picked, but we will delete this later because the player shouldn't know
  

intro()
gamestart()