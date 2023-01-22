# print(len("Hello"))
# 19
# DATA types

# # String
# print("Hello"[0])
# print("Hello"[4])

# print("123"+"345")

# # Integer int

# print(123 + 345)

# 123_456_789

# # Float double

# 3.14159

# # Boolean

# True
# False

# 21

# # Don'tchange the code below
# two_digit_number = input("Type a two digit number: ")
# # Don't change the code above

# ###################################

# # Write your codebelow this line

# # print(type(two_digit_number))
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
# result = int(first_digit) + int(second_digit)
# print(result)

# 22
# 3+5
# 7-4
# 3*2
# 6/3
# 2**3

# PEMDASLR
# ()
# * *
# * /
# + -

# print(3 * 3 + 3 / 3 - 3)
# print(3 * (3 + 3) / 3 - 3)

# 23
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")

# bmi = float(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print(bmi, bmi_as_int)

# 24
# print(round(8//3, 2))
# score = 0
# height = 1.8
# isWinning = True
# # f -String
# print(
#     f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# 25
# age = input("What is your current age: ")
# age_as_int = int(age)
# years = 90 - age_as_int
# days = years * 365
# weeks = years * 52
# months = years * 12


# print(f"You have {days} days, {weeks} weeks, and {months} months left")

# Welcome = print("Welcome to the tip calculator")
# bill = float(input("What was the total bill? $: "))
# tip = float(
#     input("What percentage tip would you like give? 10, 12 or 15?: "))
# people = int(input("How many people to split the bill?: "))
# # tips_as_persentage = tip / 100
# # total_amount_tip = bill * tips_as_persentage
# # total_bill = bill+total_amount_tip
# # bill_per_person = round(total_bill / people, 2)
# # pay_person = print(f"Each person should pay: {bill_per_person}")
# total_amount_per_person = (
#     ((tip/100) * bill) + bill) / people
# sum = "{:.2f}".format(total_amount_per_person)
# pay_person = print(
#     f"Each person should pay: {sum}")
