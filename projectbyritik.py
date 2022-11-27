import random

print("Welcome to Rock,Paper,Scissor")

user_score = 0
comp_score = 0
ties = 0

random_win_message = ["Oh no! I lost. But I will win the next match", "Oops! I lost. I will see you in the next round",
                      "You won this one, so you better watch out next time "]
random_Tie_message = ["Its a tie, but i will win the next one", "Its booring! let's play another round"]
random_lost_message = ["Hahah! I won", "GG! I won hope you have better luck next time!",
                       "Lucky me! it's my day, let's have another round"]
name = input("Enter your name here: ")

print(""" 
Winning rules:
Rock vs Paper --> Paper   
Scissors vs Paper -->Scissors
Scissors vs Rock --> Rock
""")

print("""Choices are:
1.Rock
2.Scissor
3.Paper
""")

while True:

    choice = (input("Enter your choice from 1-3: "))
    print()

    while choice != "3" and choice != "1" and choice != "2":
        choice = input("Please Enter valid input: ")
        print()
    choice = int(choice)
    if choice == 1:
        user_choice = "Rock"

    elif choice == 2:
        user_choice = "Scissors"

    else:
        user_choice = "Paper"

    print("The user choice is: ", user_choice)
    print()
    print("Now its Computer's turns: ")

    computer = random.randint(1, 3)

    if computer == 1:
        comp_choice = "Rock"

    elif computer == 2:
        comp_choice = "Scissors"

    else:
        comp_choice = "Paper"

    print()
    print("The Computer's choice is", comp_choice)
    print()

    if ((user_choice == "Paper" and comp_choice == "Rock") or (comp_choice == "Rock" and user_choice == "Paper")):
        if user_choice == "Paper" and comp_choice == "Rock":
            print(user_choice, "covers the", comp_choice)
            print(random.choice(random_win_message))
        else:
            print(comp_choice, "covers the", user_choice)
            print(random.choice(random_lost_message))
        result = "Paper"

    elif ((user_choice == "Rock" and comp_choice == "Scissors") or (
            comp_choice == "Rock" and user_choice == "Scissors")):
        if user_choice == "Rock" and comp_choice == "Scissors":
            print(user_choice, "smashes", comp_choice)
            print(random.choice(random_win_message))
        else:
            print(comp_choice, "smashes", user_choice)
            print(random.choice(random_lost_message))
        result = "Rock"

    elif (user_choice == comp_choice):
        print("It's a tie")
        print(random.choice(random_Tie_message))
        result = "Tie"

    elif ((user_choice == "Scissors" and comp_choice == "Paper") or (
            comp_choice == "Scissors" and user_choice == "Paper")):
        if user_choice == "Scissors" and comp_choice == "Paper":
            print(user_choice, "cuts", comp_choice)
            print(random.choice(random_win_message))
        else:
            print(comp_choice, "cuts", user_choice)
            print(random.choice(random_lost_message))

        result = "Scissors"

        if result == "Tie":
            ties += 1

        elif result == user_choice:
            user_score += 1
        print("You wins!!")

    else:
        comp_score += 1
        print("computer wins!!")
    print()

    print("Scores are:-")
    print(name, " 's score is: ", user_score)
    print("computer's score is: ", comp_score)
    print("Ties are", ties)

    repeat = input("Do you want to play again: ").lower()
    if repeat == "no":
        break
if user_score > comp_score:
    print("Congrulation!!! You win the game")
elif comp_score > user_score:
    print("Sorry!!! You lost The Game")
    print("Better Luck Next Time!!")

else:
    print("Nobody won the game")
print("Thanks For Playing!!")
print("See you next Time")