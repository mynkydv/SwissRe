
import random

# Make a list of words.
words = [
     'apple',
     'banana',
     'orange',
     'coconut',
     'straw berry',
     'lime',
     'lemon',
     'melon',
     'grapefruit',
     'bluebeery',
     'kumquat'
]

while True:
    
    start = input("press enter/return to start or press Q to quit ")

    if(start.upper == 'Q'):
        break


    # pick a random word.
    secret_word = random.choice(words)

    bad_guesses = []
    good_guesses = []

    while(len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word))):
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_ ', end = '')
        print('')
        print('strikes: {}/7'.format(len(bad_guesses)))
        print('')

        guess = input("Guess a letter: ").lower()

        if(len(guess) != 1):
            print("You can only guess a single letter. ")
            continue
        elif( guess in bad_guesses or guess in good_guesses):
            print("You already guessed that letter")
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")

        if guess in secret_word:
            good_guesses.append(guess)    

            if ( len(good_guesses) == len(list(secret_word))):
                print("You win the secret word was: {}".format(secret_word))

        else:
            bad_guesses.append(guess)            

    else:
        print("You didnt guess it. My secret word was {}".format(secret_word))
    
    
    # print("Guess a fruit name.")
    
    # if(randomWord.upper() == guessWord.upper()):
    #     print("You guessed correct fruit.")
    # else:
    #     print("Better luck next time. The correct word is {}".format(randomWord))