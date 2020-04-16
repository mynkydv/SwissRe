import random

words = [
    'apple',
    'mango',
    'grapefruit',
    'blueberry',
    'orange',
    'banana'
]


while True:

    choice = input("Press enter to continue Q to quit ")

    if choice.upper() == 'Q':
        break

    secret_word = random.choice(words)

    good_guess = []
    bad_guess = []

    while(len(bad_guess) < 7 and len(good_guess) != len(list(secret_word))):
        
        guess = input("Please enter a letter ")

        if(guess.isalpha() == False):
            print("Please enter only letter")
            continue
        elif(len(guess) > 1):
             print("You can enter only one letter")
             continue

        if(guess in good_guess or guess in bad_guess):
            print("You have already guessed this word")
            continue        
        
        if(guess in secret_word):
            count = secret_word.count(guess)
            good_guess.extend(guess*count)
            if ( len(good_guess) == len(list(secret_word))):
                print("You win the secret word was: {}".format(secret_word))
                break                           
        else:
             bad_guess.append(guess)
             print("strinke {}/7 ".format(len(bad_guess)))

        for letter in secret_word:
                if(letter in good_guess):
                    print(letter,end='')                
                else:
                    print("_ ", end='')
        print("")

    else:
        print("You loose!. The correct word was {}".format(secret_word))                            

                   