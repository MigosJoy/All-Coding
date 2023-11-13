# str1 = 'exterminate!'
# str2 = 'number one - the larch'

# str2.find('n')

# def square(x):
#     '''
#     x: int or float
#     '''
#     return x**2


# def fourthPower(x):
#     '''
#     x: int or float.
#     '''
#     # Your code here
#     return square(x) * square(x)


# fourthPower(3)

# def odd(x):
#     '''
#     x: int

#     returns: True if x is odd, False otherwise
#     '''
#     # Your code here
#     if x % 2 == 0:
#         y = False
#     else:
#         y = True
#     return y


# odd(3)


# def iterPower(base, exp):
#     '''
#     base: int or float
#     exp: int >= 0

#     returns: int or float, base^exp'''
#     for i in range (1, exp):
#         base *= base
#     return base
# iterPower(3,3)

# def recurPower(base, exp):
#     '''
#     base: int or float
#     exp: int >= 0

#     returns: into or float, base^exp
#     '''
#     if exp == 0:
#         return 1
#     else:
#         return base * recurPower(base, exp-1)


# recurPower(3, 4)

# def gcdIter(a,b):
#     '''
#     a, b: positive integers
#     returns: a positive integer, the greatest commond divisor of a&b.
#     '''
#     test = min(a,b)
#     for i in range(test,1,-1):
#         if b%test == 0 and a%test == 0:
#             break
#         else:
#             test -= 1
#     return test

# gcdIter(17,1)

# def gcdRecur(a, b):
#     '''
#     a, b: positive integers
#     returns: a positive integer, the greatest commond divisor of a&b.
#     '''
#     if b == 0:
#         return a
#     else:
#         return gcdRecur(b, a % b)


# gcdRecur(1071, 462)

# Exercise: Is In?

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

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    while True:
        index_num = len(aStr) // 2
        test_char = aStr[index_num]
        if aStr == '':
            return False
        elif len(aStr) == 1 and aStr == char:
            return True
        elif len(aStr) == 1 and aStr != char:
            return False
        elif test_char == char:
            return True
        else:
            if char < test_char:
                new_string = aStr[:aStr.index(test_char)]
                return isIn(char, new_string)
            else:
                new_string = aStr[aStr.index(test_char)+1:]
                return isIn(char, new_string)


isIn('z', 'abcdefghijklmnop')
