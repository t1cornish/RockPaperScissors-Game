import random
repeat = True

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while repeat:

    users_choice = input("Rock, Paper or Scissors?").lower()
    if users_choice == "r":
        users_choice = "rock"
    if users_choice == "p":
        users_choice = "paper"
    if users_choice == "s":
        users_choice = "scissors"

    computers_choice = random.choice(options)

    print(
        "Rock...\nPaper...\nScissors...\nShoot!\nYou chose " + users_choice + " and your opponent chose " + computers_choice)

    if users_choice == "rock" and computers_choice == "scissors":
        print("You Win!")
        user_score += 1

    elif users_choice == "paper" and computers_choice == "rock":
        print("You Win!")
        user_score += 1

    elif users_choice == "scissors" and computers_choice == "paper":
        print("You Win!")
        user_score += 1

    elif users_choice == "scissors" and computers_choice == "rock":
        print("You Lose!")
        computer_score += 1

    elif users_choice == "rock" and computers_choice == "paper":
        print("You Lose!")
        computer_score += 1

    elif users_choice == "paper" and computers_choice == "scissors":
        print("You Lose!")
        computer_score += 1

    elif users_choice == computers_choice:
        print("It's a Tie!")

    elif users_choice == "gun":
        print("Gun ALWAYS Wins! ")
        user_score += 1

    else:
        print("Wait a minute... you can't use that. You must only chose Rock, Paper or Scissors")

    print("You " + str(user_score) + " : " + str(computer_score) + " Opponent")

    stop = input("Do you want to play again? (Y/N)").lower()
    if stop == "n":
        repeat = False
    elif stop == "no":
        repeat = False
