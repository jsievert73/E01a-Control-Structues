#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') # prints out "Greetings!" in the terminal.
colors = ['red','orange','yellow','green','blue','violet','purple'] # creates a list of colors which will be saved for future use.
play_again = '' # creates a variable called "play_again" that is just a space at the moemnt
best_count = sys.maxsize            # the biggest number, which makes it so that the first time they play the game, they will get their best guess so far.
while (play_again != 'n' and play_again != 'no'): # will repeat the game, as long as the player has not responded negatively to playing again.
    match_color = random.choice(colors) # the program picks a random color from the list we created earlier so the game is different every time.
    count = 0 # starts a counter at 0 that will be used to check how many attempts the user had to go through in order to guess the correct color
    color = '' # creates the variable color, which will soon be replaced by the user's input.
    while (color != match_color): # will run this loop while the color does not match the randomly selected color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line      this is also taking an input from the user after printing "What is my favorite color?" in the window.
        color = color.lower().strip() # this line takes the user's guessed color and strips it of spaces as well as downcasing all letters
        count += 1 # this adds one to the count variable, tracking that the user just made a guess.
        if (color == match_color): # checks if the guessed color matches the randomly selected color.
            print('Correct!') # if so the program will print "Correct!"
        else: # if the above check does not return true, the program will run what falls under this line.
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # the program prints the text within the quotes while replacing {guesses} with the variable saved in count
    print('\nYou guessed it in {0} tries!'.format(count)) #the program prints the text within the counts and replaces {0} with the variable stored in count
    if (count < best_count): # checks if the player had to use less guesses then their best run of this game so far.
        print('This was your best guess so far!') # if the above check returns true, then the program prints the text within the quotes.
        best_count = count # if the above check returns true, the current count for this game replaces best_count as the new record.
    play_again = input("\nWould you like to play again? ").lower().strip() #checks if the player would like to play again, and strips and downcases the input to save as the play_again input
print('Thanks for playing!') #once the player has ended the game by responded with "n" or "no" the program prints the text with quotes on this line.