import random, math

# Taking Inputs
lower = int(input("Enter the Lower Limit"))
upper = int(input("Enter the Upper Limit"))

# Setting a limit to the no of guesses
guess_limit = int(round(math.log(upper - (lower + 1), 2)))

# The computer selected random no
the_no = int(random.randint(lower, upper))

print("You have ", guess_limit, "chances to guess")
count = 0

# The logic for checking for a match
while count < guess_limit:
    guess = int(input("Enter your guess"))
    if guess == the_no:
        print("Congratulations! You did it in ", count, "try")
        count = count + 1
        break
    elif guess > the_no:
        print("Try Again! You guessed too high")
        count = count + 1
    elif guess < the_no:
        print("Try Again! You guessed too small")
        count = count + 1

# When the limit is reached
    if count >= guess_limit:
        print("Better Luck Next Time!")
