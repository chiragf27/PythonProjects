import random
#game_images = [rock, paper, scissors]
u_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#print(game_images[u_choice])
c_choice = random.randint(0, 2)
print(f"Computer chose: {c_choice}")
#print(game_images[c_choice])
if u_choice >= 3 or u_choice < 0:
    print("You typed an invalid number, you lose!")
elif u_choice == 0 and c_choice == 2:
    print("You win!")
elif c_choice == 0 and u_choice == 2:
    print("You lose")
elif c_choice > u_choice:
    print("You lose")
elif u_choice > c_choice:
    print("You win!")
elif c_choice == u_choice:
    print("It's a draw")