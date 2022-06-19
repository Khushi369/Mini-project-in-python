print("Welcome to the quiz!!")
play = input("Are you ready to play? ")
if play.upper()!="YES":
    quit()

print("Lets start :)")
score = 0
answer = input("What does CPU stands for? ")
if answer.lower()=="central processing unit":
    print("Yay!!")
    score+=1
else:
    print("Wrong :(")

answer = input("full form of RAM ")
if answer.lower()=="random access memory":
    print("Yay!!")
    score+=1
else:
    print("Wrong :(")
answer = input("full form of GPU ")
if answer.lower()=="graphics processing unit":
    print("Yay!!")
    score+=1
else:
    print("Wrong :(")
answer = input("What is 6*6*6? ")
if answer==216:
    print("Yay!!")
    score+=1
else:
    print("Wrong :(")
answer = input("What is 12*12? ")
if answer==144:
    print("Yay!!")
    score+=1
else:
    print("Wrong :(")
answer = input()

print("You got" + str(score) + "questions correct")

