# 59
# print("Hello")
# num_char = len('Hello')
# print(num_char)


# def my_function():
#     print("hello")
#     print("Bye")


# my_function()

# 60 Robor solution
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def moves():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()


# def finish():
#     moves()
#     moves()
#     moves()
#     moves()
#     moves()
#     moves()


# finish()

# OR

# for finish in range(6):
#     moves()


# 61
# 62
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def moves():
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# # for finish in range(6):
#     # moves()


# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     moves()
#     number_of_hurdles -= 1
#     print(number_of_hurdles)

# Random finish
# while not at_goal():
#     moves()


# 63
# def turn_right():
#      turn_left()
#      turn_left()
#      turn_left()


# def jump():
#      turn_left()
#      move()
#      turn_right()
#      move()
#      turn_right()
#      move()
#      turn_left()

# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# 64
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()


# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()


# while not at_goal():
#     if wall_in_front():
#         jump()
#     else:
#         move()

# 65
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while front_is_clear():
#     move()
# turn_left()

# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#          move()
#     else:
#         turn_left()
