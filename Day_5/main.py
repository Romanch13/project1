# 50 for loop
# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " Pie")
# print(fruits)

# 51
# student_heights_list = [180, 124, 165, 173, 189, 169, 146]

# Don't change the code below
# student_heights = input("Input a list of students heights ").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# Don't change the code above

# Write your cide below this row
# print(sum(student_heights))
# total_height = sum(student_heights)
# number_students = len(student_heights)
# average_height = round(total_height / number_students)
# print(average_height)

# total_height = 0
# for height in student_heights:
#     total_height += height


# number_students = 0
# for student in student_heights:
#     number_students += 1


# average_height = round(total_height / number_students)
# print(
#     f"Total sum = {total_height}, Lenght item = {number_students}, Average Heights = {average_height}")

# 52
# Don't change the code below
# student_scores = input("Input a list of students heights ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # Don't change the code above
# # print(max(student_scores), min(student_scores))

# highest_score = 0
# low_score = 0
# for score in student_scores:
#     if (score > highest_score):
#         highest_score = score
# print(f"The hightst score in the class is: {highest_score}")

# 53

# ForLoop with Range
# for number in range(0, 10):
#     print(number)

# total = 0
# for number in range(1, 101):
#     total += number
# print(total)

# 54

# Write your code below this row
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

# total2 = 0
# for number in range(1, 101):
#     if (number % 2 == 0):
#         total2 += number
# print(total2)

# 55
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '/']

print("Welcome to the PyPassword generator")
nr_letters = int(input("How many Letters would you like i your password?: \n"))
nr_symbols = int(input("How many Symbols would you like?: \n"))
nr_numbers = int(input("How many Numbers would you like?: \n"))


# Eazy lvl
# password = ""
# for char in range(1, nr_letters+1):
#     password += random.choice(letters)
# for char in range(1, nr_symbols+1):
#     password += random.choice(symbols)
# for char in range(1, nr_numbers+1):
#     password += random.choice(numbers)


# Hard lvl
password_list = []
for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))
for char in range(1, nr_symbols+1):
    password_list.append(random.choice(symbols))
for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)
# print(f"Here is your password: {password_list} ")

password = ''
for char in password_list:
    password += char
print(f"Here is your password: {password} ")
