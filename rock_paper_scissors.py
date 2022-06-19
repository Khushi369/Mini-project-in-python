import random

user = 0
computer = 0

options  =  ["rock","paper","scissors"]
while True:
    user_in = input("rock\paper/scissors or q to quit: ").lower()
    if user_in == "q":
        quit()

    if user_in not in ["rock","paper","scissors"]:
        continue

    random_num = random.randit(0,2)
    computer_pick = options[random_num]
    print("computer picked" computer_pick +".")

    if user_in=="rock" and computer_pick == "scissors":
        print("You won!!")
        user+=1
    elif user_in=="paper" and computer_pick == "rock":
        print("You won!!")
        user+=1
    elif user_in=="scissors" and computer_pick == "paper":
        print("You won!!")
        user+=1
    else:
        print("You lost!")
        computer+=1

print("You won", user, "times")
print("Computer won", computer, "times")
print("Goodbye!!")
