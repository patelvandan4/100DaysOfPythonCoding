print("Welcome to the rock paper and scisssors games!!")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
import random
img = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, Type 1 for paper, Type 2 for scissors = "))
computer_choice = random.randint(0, 2)
print(f"User Chose {user_choice}.")
print(img [user_choice])
print(f"Computer Chose {computer_choice}.")
print(img [computer_choice])
if user_choice == 0 and computer_choice == 0:
    print("It is a draw match. Start Again")
elif user_choice == 0 and computer_choice == 1:
    print("Computer wins and user loses the match. Try again")
elif user_choice == 0 and computer_choice == 2:
    print("User Wins and Computer loses the game")
elif user_choice == 1 and computer_choice == 0:
    print("User wins and computer loses the game")
elif user_choice == 1 and computer_choice == 1:
    print("It is a draw match. Start again")
elif user_choice == 1 and computer_choice == 2:
    print("Computer Wins and User Loses the game. Try again")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins and user loses the game. Try again")
elif user_choice == 2 and computer_choice == 1:
    print("User wins the game Yayyy")
elif user_choice == 2 and computer_choice == 2:
    print("It is a draw match. Start again")
else:
    print("Invalid Input plese select 0 for rock and 1 for paper and 2 for scissors.")


