# 29
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# # > < >= <= == !=
# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry? you have to grow taller before you can ride")

# 30
# Don't change the code below

# number = int(input("Which number do you want to change"))

# # Don't change the code above

# # Write your code below this line

# if number % 2 == 0:
#     print("This is a even nuber")
# else:
#     print("This is an add number")

# % - module operator
# 7%2  2+2+2+1

# 31
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("what is your age? "))
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry? you have to grow taller before you can ride")

# 32
# Welcome = print("Welcome to the calculator")

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# bmi = float(weight) / float(height) ** 2
# bmi_int = round(bmi, 2)
# print(bmi_int)

# if bmi_int < 18.5:
#     print(f"Your bmi is {bmi_int}, underweight ")
# elif bmi_int < 25:
#     print(f"Your bmi is {bmi_int}, Normal Weight ")
# elif bmi_int < 30:
#     print(f"Your bmi is {bmi_int}, Overweight ")
# elif bmi_int < 35:
#     print(f"Your bmi is {bmi_int}, obese ")
# else:
#     print(f"Your bmi is {bmi_int}, clinically obese ")

# 33
# year = int(input("Which year do you want to check"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not Leap year.")
#     else:
#         print("Leap year")
# else:
#     print("Not Leap year.")

# 34
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("what is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("youth tickets are $7.")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     wants_photo = input("Do you wwant  photo taken? Y or N. ")
#     if wants_photo == 'Y' or 'y':
#         # Add $3 to thier bill
#         bill += 3
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry? you have to grow taller before you can ride")

# 35
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N:  ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25


# if add_pepperoni == 'Y':
#     # Add papperoni Small pizza 2$
#     if size == "S":
#         bill += 2
#     else:
#         # Add papperoni Medium and Large pizza 3$
#         bill += 3

# if extra_cheese == 'Y':
#     bill += 1

# print(f"Your final bill is {bill}")

# 36
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster!")
#     age = int(input("what is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         print("youth tickets are $7.")
#     elif age >= 45 and age <= 55:
#         print("everything is going to be ok. Have a free ride on us! ")
#     else:
#         bill = 12
#         print("Adult tickets are $12.")

#     wants_photo = input("Do you wwant  photo taken? Y or N. ")
#     if wants_photo == 'Y' or 'y':
#         # Add $3 to thier bill
#         bill += 3
#     print(f"Your final bill is {bill}")
# else:
#     print("Sorry? you have to grow taller before you can ride")

# 37
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combine_string = name1 + name2
# lower_case_string = combine_string.lower()

# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")

# true = t + r + u + e

# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")

# love = l + o + v + e

# love_score = int(str(true) + str(love))

# print(love_score)

# if (love_score < 10) and (love_score > 90):
#     print(
#         f"Your love score is {love_score}, you go together like coke and mentos.")
# elif (love_score >= 40) or (love_score <= 50):
#     print(f"Your love score is {love_score}, you are alright together.")

# else:
#     print(f" Your score is {love_score}")

# 38
# print("Welcome to Tresure Island")
# print("Your mission is to find the Treasure")
# choose1 = input(
#     "You're at a cross road. Where do tou want to go? Type "'"left"'" or "'"right"'" \n").lower()

# if choose1 == "left":
#     # Continue in the game
#     choose2 = input(
#         "You come to a lake. There is an island in the middle of the lake. Type "'"wait"'" to wait for a boat. Type "'"swim"'" too swim across \n").lower()
#     if choose2 == "wait":
#         choose3 = input(
#             "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
#         if choose3 == "red":
#             print("It's a room full of fire. Game Over")
#         elif choose3 == "yellow":
#             print("You find the Treasure. You WIN!")
#         elif choose3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over")
#     else:
#         print("You got attacked by an angry trout. Game over")
# else:
#     print("You fell into a hole. Game over")
