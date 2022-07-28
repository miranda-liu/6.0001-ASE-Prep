# varA = -5
# varB = -10
# print(type(varA))

# if type(varA) == "str" or type(varB) == "str":
#     print("string involved")
# elif varA > varB:
#     print("bigger")
# elif varA == varB:
#   print("equal")
# elif varA < varB:
#   print("smaller")

# divisor = 2
# for num in range(0, 10, 2):
#     print(num/divisor) 

# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0

# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#        or char == 'o' or char == 'u':
#         numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1

# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons)) 

# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#         break

# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# x = 25
# epsilon = 0.01
# step = 0.1
# guess = 0.0

# while guess <= x:
#     if abs(guess**2 -x) >= epsilon:
#         guess += step
#     print(guess)
#     break

# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))

# enumerative search
# x = 23
# epsilon = 0.01
# step = 0.1
# guess = 0.0

# while abs(guess**2-x) >= epsilon:
#     if guess <= x:
#         guess += step
#     else:
#         break

# if abs(guess**2 - x) >= epsilon:
#     print('failed')
# else:
#     print('succeeded: ' + str(guess))


# bisection search
# Please think of a number between 0 and 100!
# Is your secret number 50?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 75?
# Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
# Is your secret number 87?
   # print("Is your secret number " + str(current_num) + "?")

print("Please think of a number between 0 and 100!")
guess = False
low = 0
high = 100
ans = (high+low)/2.0
while guess == False:
    print("Is your secret number" + ans + "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    if user_input == "h":
        high = ans
    elif user_input == "l":
        low = ans
    elif user_input == "c":
        guess = True
        print("Game over. Your secret number was: " + ans)
    else:
        print("Sorry, I did not understand your input.")
    ans = (high+low)/2.0




