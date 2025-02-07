import random

def guess_random():
    print('Hello! What is your name?')
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    num = random.randint(1, 20)
    cnt = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        cnt += 1
        if guess < num:
            print("Your guess is too low.")
        elif guess > num:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
            break 
guess_random()