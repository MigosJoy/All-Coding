# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0

# while guess <= x:
#     if abs(guess**2 -x) < epsilon:
#         break
#     else:
#         guess += step

# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))

# # Notice how if we have two print statements
# print("Hi")
# print("there")

# # The output will have each string on a separate line:
# Hi
# there

# # Now try adding the following:
# print("Hi",end='')
# print("there")
# print("Hi",end='*')
# print("there")

# # The output will place the subsequent string on the same line
# # and will connect the two prints with the character given by end
# Hithere
# Hi*there

# # Practice Problem
# print("Please think of a number between 0 and 100!")
# x = 100
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = x
# ans = (high + low)/2.0

# while True:
#     print('Is your secret number ' + str(int(ans)) + '?')
#     secret_num = str(input('Enter "h" to indicate the guess is too high. Enter "l" to indicated the guess is too low. Enter "c" to indicate I guessed correctly.'))
#     numGuesses += 1
#     if secret_num == 'c':
#         break
#     elif secret_num == 'h':
#         high = ans
#     elif secret_num == 'l':
#         low = ans
#     else:
#         print('Sorry I did not understand your input')
#     ans = (high + low)//2.0
# print('Game Over. Your secret number was: ' + str(int(ans)))
