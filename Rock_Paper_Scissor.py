import random

rule = """Winning Rules of the RPS Game is as follows:
                    rock vs paper -> paper wins
                    rock vs scissors -> rock wins
                    paper vs scissors -> scissors wins."""
print(rule)

# Logic for deciding who wins
while True:
    user_c = int(input("Enter your choice: 1. Rock, 2. Paper or 3. Scissor \n"))
    comp_c = random.randint(1, 3)
    print(comp_c)
    choice_list1 = {'1': 'Rock', '2': 'Paper', '3': 'Scissor'}
    print("User choice is", choice_list1.get(str(user_c)))
    print("Computer choice is:", choice_list1.get(str(comp_c)))

    if user_c != comp_c:
        if (user_c == 1 and comp_c == 2) or (user_c == 2 and comp_c == 1):
            print("Paper Wins")
        elif (user_c == 1 and comp_c == 3) or (user_c == 3 and comp_c == 1):
            print("Rock Wins")
        else:
            print("Scissor Wins")
    else:
        print("Same choice. Go again")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("Thanks for playing")
