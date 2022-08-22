import random
#Declaring options and initializing user wins and computer wins to 0

user_wins = 0
computer_wins = 0
options=["stone","paper","scissors"]
#Snippet code for user input

while True:
    user_input = input("Type Stone/Paper/Scissors or Q to quit ").lower()
    if user_input == "q":
        print("Bye!")
        break
    if user_input not in options:
        print("!!!Enter valid option!!!")
        continue
#Snippet code for logic

    random_number = random.randint(0, 2)
    #stone:0,paper:1,scissors-2
    computer_pick = options[random_number]
    print("Computer picked",computer_pick +".")

    if user_input == "stone" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "stone":
        print("You won!")
        user_wins += 1
    
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "scissors":
        print("Draw!")

    elif user_input == "paper" and computer_pick == "paper":
        print("Draw!")
        
    elif user_input == "stone" and computer_pick == "stone":
        print("Draw!")

    else:
        print("You lost!")
        computer_wins +=1
#Snippet code for score

print("You won", user_wins, "times")
print("The computer won", computer_wins, "times")

if(user_wins>computer_wins):
 print("you won the match !")

elif(user_wins<computer_wins):
 print("You lost the match !")

else:
 print("Match draw !")
