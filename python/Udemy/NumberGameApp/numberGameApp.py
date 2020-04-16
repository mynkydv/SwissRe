import random

# Generate random number between 1 and 10
# Get a number guess from player
# Compare guess with secret number
# show result
# Ask if want to try again


def get_randon_numer():
    return random.randint(1,10)

while True:
    print("Please guess secret number between 1 and 10")
    try:
        guessNumber = int(input(">"))
    except:
        print("Not a valid entry.")
        continue
    secretNumber = get_randon_numer()
    if(guessNumber == secretNumber):
        print("Buzzinga !! You guessed it correct.")
    else:
        print("Better luck next time :(. The correct answer is {}".format(secretNumber))
    
    print("Do you want to continue: Y/N")
    choice = input(">")

    if(choice.upper() == "Y"):
        continue
    elif(choice.upper() == "N"):
        break
    else:
        print("Incorrect choice.")
        

        