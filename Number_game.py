# Write a Python Program to create a Guess the number game. You can use different modules and functions to create this game. Every time the user guesses wrong, drop a hint. You can drop additional hints as well.

import random
print("Guess a number between 1-100")
original_num= random.randint(1,100)
run= True
while run:
    user_input= int(input("Enter your guess:"))
    if user_input< original_num:
        print("Your guess is wrong. The real number is higher.")
    elif user_input>original_num:
        print("Your guess is wrong. The real number is lower than this number.")
    elif user_input==original_num:
        print("You guess it right. You won!!!")
        run= False
        break
    else:
        print("Invalid input")    
