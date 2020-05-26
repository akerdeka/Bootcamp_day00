import sys
import string
import random


def guess():
    n = random.randint(1, 99)
    attempts = 1
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!\n")
    print("What's your guess between 1 and 99?")
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == 'exit':
            print("Good bye !")
            break
        if line.isdigit():
            if int(line) > n:
                print("Too high !\n")
                attempts += 1
            elif int(line) < n:
                print("Too low !\n")
                attempts += 1
            else:
                if attempts == 1:
                    print("Congratulations! You got it on your first try!")
                else:
                    print("Congratulations, you won in {} attempts !".format(attempts))
                if n == 42:
                    print("The answer to the ultimate question of life, the universe and everything is 42.")
                break
        else:
            print("That's not a number.")
        print("What's your guess between 1 and 99?")
    return


guess()
