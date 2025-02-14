





# if you have a list and want to loop through it using a function
#     using for loop
# def loopin(password):
#     if len(password) > 8:
#         return True
#     else:
#         return False
#
# password_list = ["dgergerg", "gegregreg", "rtyuiiuoil", "ky6ktjkt"]
#
# for password in password_list:
#      result = loopin(password)
#      print(result)
#


#
# def add_odd_numbers():
#     total = 0
#     for number in range(1,101,2):
#       total += number
#     return total
#
#
# result = add_odd_numbers()
# print(result)

#
# def add_even_numbers(start, end):
#     total = 0
#     for number in range(1, 100):
#         total += number
#     return total
#
#
# result = add_even_numbers(1, 100)
# print(result)

#
# username = ""
# while username != "test":
#     input(f"enter username: {username}")
# username = ""
# while username != "test":
#     username = input(f"Enter username: ")
#
# list = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
# def numbers_divisible_byfive(p_list):
#
#     for list in p_list:
#         if list > 130:
#             print("stop")
#             break
#         if (list % 5 == 0):
#             print(list)
#
#
#
#
# numbers_divisible_byfive(list)
# #print(result)

# import math
#
# p_num = int(input("enter number: "))
# def factorial(p_num):
#     if p_num == 0:
#         return 1
#     elif p_num <= 0:
#         return "Factorial does not exist for neagative numbers"
#     else:
#         return math.factorial(p_num)
#
#
# result = factorial(p_num)
# print(f"The factorial of {p_num} is {result}")


# numbers = 0
# total = 0
#
# def check_number(numbers):
#     count = 0
#     while numbers != "done":
#         numbers = input("enter a number: ")
#         try:
#             if numbers != "done":
#                 numbers = int(input("enter a number: "))
#         except:
#             print("Error, please enter numeric input: ")
#         continue
#
#         count += 1
#         result = total + numbers
#         average = float(result / count)
#         continue


# check_number(numbers)

# numbers = 0
# def check_number(numbers):
#     try:
#         float(numbers)
#         return numbers
#
#     except(ValueError, TypeError):
#         print("Error, please enter numeric input: ")
#         return False
#
#
#     while True:
#         p_numbers = int(input("enter a number: "))

#
# def numbers(p_num):
#     numbers = [] # initialise empty list to store the numbers
#     while True:
#         num = int(input("enter a number: "))
#         numbers.append(num)
#         if num == "done":
#             break
#             max(numbers)
#             min(numbers)
#             print(f"maximun number: {max(numbers)} , minimum numbers: {min(numbers)}")
#
# numbers(num)

# def perform_division(a,b):
#     return a/b
#
# result = perform_division(16,2)
# print(result)
#
# import random
#
# ran_num = random.randint(1, 20)
# print(ran_num)


#
#
#
# import random
#
# # Generate a random number between 1 and 6 (inclusive)
# ran_num = random.randint(1, 6)
#
# # Print the random number using an f-string
# print(f"Dice1: {ran_num}")
#

#
# def sum_of_two_digits():
#     a = input("enter 2 digits number : ")
#     sum = int(a[0]) + int(a[1])
#     return sum
#
#
# result = sum_of_two_digits()
# print(result)

#
# fruit = "apple"
# counter = 0
# while counter < len(fruit):
#     result = fruit[counter]
#     print(result)
#     counter +=1

# str = input("enter a string: ")
# entry = str
# counter = 0
# while counter < len(entry):
#     result = str[counter]
#     print(
#         result)
#     counter += 1
#
#
# number = input("Enter an integer number: ")
# sum_digits = 0
# for num in number:
#     sum_digits = sum_digits + int(num)

# print(sum_digits)
# def count_letter(word, letter):
#     word = input("enter any word: ")
#     letter = input("enter any letter")
# #     for letter in word:
# #         return
# custom_string = "I love python."
# print(custom_string.replace(".", "!"))
# #print(dir(custom_string))
#
# name = "John"
# age = 25
# print("{:<10}  {:>5}".format(name, age))  # Left and right alignment
# print(f"{name:<10}  {age:>5}")
# ..............................................................
# pi = 3.14159265359
# print(f"Pi to 3 decimal places: {pi:.3f}")
# print(f"Pi with padding: {pi:10.3f}")
#
# ...................................................................
# from string import Template
# template = Template("Hello, $name! You are $age years old.")
# formatted_string = template.substitute(name="Eve", age=28)
# print(formatted_string)
# ..............................................................
#
# x = 10
# y = 20
# print(f"The sum of {x} and {y} is {x + y}.")
# print(...................................................)
#
# name = "Alice"
# age = 30
# print("Hello, %s! You are %d years old." % (name, age))

# fruit = "banana"
# l = len(fruit)
# #print(l)
# print(fruit[l-1])
#
# new = "Hello python"
# print(new[1:7])

#
# def sum_of_two_digits():
#     num = input("Enter two digits number : ")
#     return int(num[0]) + int(num[1])
#
#
#
# result = sum_of_two_digits()
# print(result)










#
# fruit = "apple"
#
# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index += 1
#
# ................................


#
# str = input("enter a string: ")
#
# counter = 0
# while counter < len(str):
#    result = str[counter - 1]
#    print(result)
#    counter +=1



# number = input("Enter number: ")
# counter = 0
# for num in number:
#     counter = counter + int(num)
#
# print(counter)

# def count_letter(word,letter):
#
#     count = 0
#     for lett in word:
#         if lett == letter:
#             count = count + 1
#     return count
#
# print(count_letter("Learig Pytho", "n"))

# def first_last_characters(word):
#         if len(word) < 2:
#             return ""
#
#         first_chart =  (word[:2])
#         second_chart = (word[-2:])
#         print(first_chart , second_chart)
#
#
#
# first_last_characters("appmillers")

# my_name = "Teejay"


# custom_string = 'I love Python.'
# result = custom_string.replace(".", "!")
#
# print(result)
#


# #def print_pattern(n):
# def print_pattern(n):
#     for i in range(0,n):
#         for j in range(0, i +1):
#               print( "*", end = ' ')
#         print()
#
#
#     for i in range(n, 0, -1 ):
#         for j in range(0, i-1):
#             print("*", end = ' ')
#         print()
#
# print_pattern(5)
#
#
#
#
# x = 5
# for i in range(0,x):
#     for j in range(0,i+1):
#          print("A", "B", )
#     #print()


# for i in range(x, 0, -1):
#     for j in range(0,i-1):
#          print("A", "B", end = ' ')
#     print()


# import math
#
#
#
# def square_list(p_list):
#
#     for i in range(len(p_list)):
#          p_list[i]  = p_list[i] ** p_list[i]
#     return p_list
#
#
# result = square_list([1,2,3])
#
# print(result)
# #
# vegetables = ["Tomato", "Cucumber", "Broccoli", "Onion", "Garlic"]
# veg = vegetables[3:4]
# print(veg)
# # custom_list = [1,2,3,4,5,6,7,8,9,10]
# # reverse_list = custom_list[::-1]
# # print(reverse_list)

# def type_list(p_list):
#
#     count = 0
#     for one_list in p_list:
#         if len(one_list) >= 2:
#             if one_list[0] == one_list[-1]:
#                 count +=1
#     return count
#
#
# result = type_list(['cbc', 'xyz', 'aba', '2332', 'abc'])
# print(result)

#
# def list1(list_one):
#     total_list = []
#
#     for num1 in list_one:
#         new_num = list1[]
#            total_list.append(num1)
#
#     # for num2 in list_two:
#     #     if num2 % 2 == 0:
#     #         total_list.append(num2)
#
#     return total_list
#
# result = list1([4, 12, 16, 21, 24, 28, 32])
# print(result)
#



# custom_list = [10, 44, 57, 99, 11, 33, 84]
# slice_1 = custom_list[:4]
# slice_2 = custom_list[4+1:]
# custom_list1 = slice_1 + slice_2
# print(custom_list1)
# slice_3 = custom_list1[:2]
# slice_4 = custom_list1[2:]
# custom_list2 = custom_list1[:2] + [11] + custom_list1[2:]
# print(custom_list2)
#
#coding exercise 42
# sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]
# chunk_1 = sample_list[:3]
# chunk_2 = sample_list[3:6]
# chunk_3 = sample_list[6:]
# print(chunk_1[::-1])
# print(chunk_2[::-1])
# print(chunk_3[::-1])

# exercise No 142
# custom_list = [1, 2, 3, 4, 5]
# custom_list = "|".join(str(item) for item in custom_list)
# print(custom_list)


#code exercise 43
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].insert(1,7000)
# print(list1)

#coding execise 44                        2
#          0    1     0    1     2    3     4     5     6    3    4
#                           0     1     2
# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# list1[2][1][2].extend(["h", "i", "j"])
# print(list1)

#exercise 46
#
# def concatenate(list_1, list_2):
#     con_1 = list_1[0] + list_2[0],
#     con_2 = list_1[0] + list_2[1],
#     con_3 = list_1[1] + list_2[0],
#     con_4 = list_1[1] + list_2[1],
#
#     return [con_1 + con_2 + con_3 + con_4]
#
#
# result = concatenate (list_1=["Hello ", "take "], list_2=["Dear", "Sir"])
# print(result)
#

# import random
# def print_map(p_map):
#     print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))
#
# map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
# print("This is our initial map...")
# print_map(map1)
#
#
#
#
# user_input = input("What do you think: where is the Golden Star in the map? ")
#
# #convert user input to a list of integers
# num_list = list(map(int, user_input))
#
# #need 2 variables , each to hold spot for row and column and also generate numbers
# row_number_generated = random.randint(0,2)
# column_number_generated = random.randint(0,2)
#
#
#
# #equate both generated numbers to "*"/ or place star on map
# map1[row_number_generated][column_number_generated] = "*"
#
# #concertenate both numbers and print generated location
# print(str(row_number_generated+1) + " " + str(column_number_generated+1))
#
# # assign a variable to the above concatenation
# computer_position = str(row_number_generated+1) + " " + str(column_number_generated+1)
#
# #compare user input with generated position
# if user_input == computer_position:
#     print("congratulations , you found the gold star!")
#
#     # for user input
# else:
#
#
#     row_number = num_list[0] -1
#     vertical_number =  num_list[1]-1
#     map1[row_number][vertical_number]= "x"
#
#     print("unfortunately, you couldnt find it. ")
#
#
#
# #map1[user_input[0]][user_input[1]] == "x"
#
#
# #print updated grid
# print_map(map1)
#

# a = 20
# b = 10
# # make a = 10 and b = 20
# c = 20
# #a is now empty
# a = 10
# # b is now empty
# b = 20
# # c is now empty
#
# print(a)
# print(b)



# years = int(input("enter year: "))
# weeks = years * 52
#
#
#
# print(" There are " +   str(weeks) + " in" +  " " + str(years) + " years")
# my_cars = []
# name_of_cars = input("enter your cars: " )
# my_cars.append(name_of_cars)
# for car in (my_cars):
#     print(car)
#
#
# my_cars = []  # Initialize an empty list
# name_of_cars = input("Enter your cars: ")  # Take input for cars
# my_cars.append(name_of_cars)  # Add the input to the list
#
# # Print each car in the list
# for car in my_cars:
#     print(car)
#
# # Define the list of strings
# hierarchy = [
#     "user_input_1",
#     "computer_generated_1",
#     "user_input_2",
#     "computer_generated_2",
# ]
#
# # Simulating user input and computer-generated string
# user_input = input("Enter your string: ")
# computer_generated = "computer_generated_example"  # Example of computer-generated string
#
# # # Add both inputs to the hierarchy list (or compare directly)
# # hierarchy.append(user_input)
# # hierarchy.append(computer_generated)
#
# # Compare the strings lexicographically
# if user_input > computer_generated:
#     print(f"The user string '{user_input}' is greater than the computer string '{computer_generated}'.")
# elif user_input < computer_generated:
#     print(f"The computer string '{computer_generated}' is greater than the user string '{user_input}'.")
# else:
#     print(f"The user string '{user_input}' is equal to the computer string '{computer_generated}'.")
#
# # Display the hierarchy list
# print("\nUpdated hierarchy list:")
# print(hierarchy)
# import random
#
# rock = 2
# paper = 3
# scissor = 1
#
# all_selection = ["rock", "paper", "scissor"]
#
# # First round of input
# user_input = input("Enter a choice (rock, paper or scissors): ")
# computer_selection = random.choice(all_selection)
#
# print(f"You choose {user_input}, Computer choose {computer_selection}")
# if user_input == computer_selection:
#     print("It is a tie!")
# elif user_input == "Rock" and computer_selection == "Scissor":
#     print("Rock is greater than Scissor, you win!")
# elif user_input == "paper" and computer_selection == "scissor":
#     print("Scissor is greater than Paper, you wins!")
# elif user_input == "Scissor" and computer_selection == "Rock":
#     print("Rock is greater than Scissor, computer wins!")
# elif user_input == "Scissor" and computer_selection == "Paper":
#     print("Scissor is greater than Paper, you win!")
# elif user_input == "Paper" and computer_selection == "Rock":
#     print("Paper is greater than Rock, you win!")
# elif user_input == "Rock" and computer_selection == "Paper":
#     print("paper is greater than rock, computer win!")
#
# # Ask if the user wants to play again
# user_input_2 = input("Play again (Y/N)? ")
#
# # While loop to continue or stop based on user input
# while user_input_2 == "Y":
#     user_input = input("Enter a choice (rock, paper or scissors): ")
#     computer_selection = random.choice(all_selection)
#     print(f"You choose {user_input}, Computer choose {computer_selection}")
#
#     if user_input == computer_selection:
#         print("It is a tie!")
#     elif user_input == "rock" and computer_selection == "scissor":
#         print("Rock is greater than Scissor, you win!")
#     elif user_input == "paper" and computer_selection == "scissor":
#         print("Scissor is greater than Paper, you wins!")
#     elif user_input == "scissor" and computer_selection == "rock":
#         print("Rock is greater than Scissor, computer wins!")
#     elif user_input == "scissor" and computer_selection == "paper":
#         print("Scissor is greater than Paper, computer win!")
#     elif user_input == "Paper" and computer_selection == "Rock":
#         print("Paper is greater than Rock, you win!")
#     elif user_input == "Rock" and computer_selection == "Paper":
#         print("paper is greater than rock, computer win!")
#
#     # After a round, ask if they want to play again
#     user_input_2 = input("Play again (Y/N)? ")
#
# print("Thanks for playing!")


# user_input = input("Enter number: ")
# digits = 0
# for sum in user_input:
#     digits = int(digits) + int(sum)
# print(digits)
#

# def count_letter(word, letter):
#     index = 0
#     count = 0
#     while index < len(word):
#         word[index]
#
#         if letter in word[index]:
#             count += 1
#         index += 1
#     return count
#
# result = count_letter("afronation","r")
# print(result)
# user_name = input("enter names: ")
# letter = 7
#
# print(user_name[letter])

# word = "Hello, World!"
# print(word[0:6])



# def print_pattern(n):
#     for num in range(0, n):
#         for num1 in range(0, num + 1):
#             print("#", end= ' ')
#         print()
# print_pattern(5)

# Implement a function that takes a list as a
# parameter and turn list items into their square.
#
# Example
#
# custom_list = [1,2,3,4,5]
# square_list(custom_list)


# def square_list(p_list):
#     new_list = []
#     for listing in p_list:
#         new_list.append(listing ** 2)
#     return new_list
# print(square_list([9,6]))
#
# food = ["rice","beans", "potato"]
# type_food = len(food)
# print(type_food)
# print(food[type_food - 1])
#
# custom_list = [1,2,3,4,5,6,7,8,9,10]
# new_list = custom_list[::-1]
# print(new_list)
#
# def count_words(p_list):
#     count = 0
#     for index in p_list:
#         if len(index) >= 2 and index[0] == index[-1]:
#
#                 count += 1
#     return count
#
# result = count_words(['cbc', 'xyz', 'aba', '2332', 'abc'])
# print(result)
#
# list_one = [4, 12, 16, 21, 24, 28, 32]
# list_two = [5, 10, 15, 20, 25, 30, 35]
#
# list_3 = []
# for index in list_one:
#     if index % 2 == 0:
#         list_3.append(index)
# for index_1 in list_two:
#     if index_1 % 2 != 0:
#         list_3.append(index_1)
#
# print(list_3)


# list_one = [4, 12, 16, 21, 24, 28, 32]
# new_var = list_one[:4]
# #print(new_var)
# few_var = list_one[5:]
# #print(few_var)
# list_one = new_var + few_var
# print(list_one)
#
# custom_list = [10, 44, 57, 99, 11, 33, 84]
# slice_1 = custom_list[:4]
# slice_2 = custom_list[5:]
# custom_list = slice_1 + slice_2
# print(custom_list)

# sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]
# # chunk_1 = sample_list[:3]
# # chunk_2 = sample_list[3:6]
# # chunk_3 = sample_list[6:]
# # print(chunk_1[::-1])
# # print(chunk_2[::-1])
# # print(chunk_3[::-1])
# print(sample_list[::-1])

custom_list = [1, 2, 3, 4, 5]
#custom_list1 = "|".join(str(item) for item in custom_list)
new_list = []
for chk_list in custom_list:
    new_list.append(str(chk_list))
cus_list =  "|".join(new_list)
print(cus_list)
