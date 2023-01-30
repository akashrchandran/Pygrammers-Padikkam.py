import random

print("Guess the number!")
print("Rules:")
print("1. The number is between 0-100")
print("2. You get only 3 chances to guess the number then your out")
print("Let's start!!", end="\n\n")
number = random.randint(1, 99)
prev_guess = []
while len(prev_guess) < 3:
    guess = int(input(f"Enter your {len(prev_guess)+1} Guess: "))
    if guess == number:
        print(f"You have guessed it correctly {number} ✅")
        break
    else:
        prev_guess.append(guess)
        for x, y in enumerate(prev_guess, start=1):
            print(f"{x}. {y} ❌")
else:
    print("Game Over ☠️")
