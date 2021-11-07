# import random

# def GuessingGame(x):
#     guessNumber = random.randint(1,x)

#     guess = 0 
#     while (guess != guessNumber):
#         guess = int(input(f"Guess a Number between 1 to {x} "))
#         if guess<guessNumber:
#             print("Too Low")
#         elif guess>guessNumber:
#             print("Too High")
#     print(f"You Won You Guessed the {x} correctly!")

# GuessingGame(10)


import random

def GuessGame(x):
    Number = random.randint(1,x)
    

    guess = 0
    while (Number != guess):
        guess = int(input("Enter Your Number between 1 to {x} : "))
        if guess > Number:
            print("Too High")
        elif guess < Number:
            print("Too Low")

    print(f"You Won! You Guessed Corectly {x}")

    GuessGame(10)