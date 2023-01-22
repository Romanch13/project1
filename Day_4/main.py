# 41
import random


# random_int = random.randint(1, 10)
# print(random_int)

# random_float = random.random()*5
# print(round(random_float, 2))

# # random_float = random.uniform(0, 10)
# # print(round(random_float, 2))

# love_score = random.randint(1, 100)
# print(f"Your favorite score is {love_score}")

# 42

# print("Welcome Calc")

# random_int = random.randint(0, 1)
# if random_int == 1:
#     print(f"Win {random_int} Heads")
# else:
#     print(f"Win Tails {random_int}")

# 43

# states_of_america = ["Delaware", "Pennsylvania",
#                      "Nevada", "Hawaii", "Iowa", "Texas", "kansas"]

# states_of_america[1] = "Pennsylvania"
# # states_of_america.append("NewYork")
# states_of_america.extend(["New-York", "Los AngeLes"])

# print(states_of_america)

# 44
# names_string = input("Give me everybody's names, separated by a comma.c \n")
# names = names_string.split(",")

# # num_items = len(names)
# # random_choice = random.randint(0, num_items - 1)
# # # print(random_choice)
# # person_who_will_pay = names[random_choice]

# person_who_will_pay = random.choice(names)
# print(person_who_will_pay + " is going to buy the meal today")

# 45
# states_of_america = ["Delaware", "Pennsylvania",
#                      "Nevada", "Hawaii", "Iowa", "Texas", "kansas"]

# num_of_states = len(states_of_america)
# print(states_of_america[num_of_states - 1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
#                "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples",
#           "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

# 46 Challenge

# row1 = ["🟧", "🟧", "🟧"]
# row2 = ["🟧", "🟧", "🟧"]
# row3 = ["🟧", "🟧", "🟧"]

# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where dou you want to put the treasure? \n")

# # Write your code below this row 👇🏽

# horizontal = int(position[0])  # 2
# vertical = int(position[1])  # 3

# # selected_row = map[vertical - 1]
# # selected_row[horizontal - 1] = "X"
# map[vertical - 1][horizontal - 1] = "X"

# # Write your code above this row 👆🏽

# # Don't change the code below
# print(f"{row1}\n{row2}\n{row3}")

# 47

rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
        ________)
---.__________)
 '''

scissors = '''
    _______
---'  _____)_____
          _______)
        __________)
       (_____)
---.___(___)
'''

game_images = [rock, paper, scissors]
user_choose = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if user_choose >= 3 or user_choose < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choose])

    computer_choice = random.randint(0, 2)
    print("Computer choice: ")
    print(game_images[computer_choice])

    if (user_choose == 0) and computer_choice == 2:
        print("User Win")
    elif (computer_choice == 0) and user_choose == 2:
        print("User lose")
    elif computer_choice > user_choose:
        print("Computer win")
    elif computer_choice < user_choose:
        print("User win")
    else:
        print("It's a draw")
