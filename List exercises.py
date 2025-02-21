# 1. Append & Extend
# Task:
# Create a list of numbers
# from 1 to 5. Then, do the following:
#
# Append the number 6 to the list.
# Extend the list with [7, 8, 9].
# Print the updated list.

list_numbers = [1, 2, 3, 4, 5]
list_numbers.append(6)
list_numbers.extend([7, 8, 9])
print(list_numbers)

# 2. Remove & Pop
# Task:
# Given the list fruits = ["apple", "banana", "cherry", "mango", "orange"], do the following:
#
# Remove "banana" using .remove().
# Remove the last element using .pop().
# Print the final list.

fruits = ["apple", "banana", "cherry", "mango", "orange"]
fruits.remove("banana")
fruits.pop((4) - 1)
print(fruits)

# 3. Find Index & Count Occurrences
# Task:
# Given nums = [3, 7, 3, 9, 3, 5, 3], do the following:
#
# Find the index of the first occurrence of 9.
# Count how many times 3 appears in the list.

nums = [3, 7, 3, 9, 3, 5, 3]

print(nums.index(9))
count = 0
for number in range(len(nums)):
    if nums[number] == 3:
        count += 1
print(count)

# 4.List Slicing
# Task:
# Given letters = ["a", "b", "c", "d", "e", "f", "g"], do the following:
#
# Print the first 3 elements using slicing.
# Print the last 3 elements using slicing.
# Print the list in reverse order using slicing.

letters = ["a", "b", "c", "d", "e", "f", "g"]
first_three = letters[:3]
print(first_three)
last_three = letters[-3:]
print(last_three)
reverse_order = letters[::-1]
print(reverse_order)

# 5. Check if Element Exists
# Task:
# Write a Python program that takes a list of city
# names and asks the user to input a city name.
# The program should check if the city exists in
# the list and print "City Found" or "City Not Found".

city_list = ["Tokyo", "Lagos", "Doha", "Accra", "london"]
user_input = input("enter city: ")
for city in range(len(city_list)):
    if user_input == city_list[city]:
        print("City found")


if user_input != city_list[city]:
    print("city not found")

#  Filter Even & Odd Numbers
# Task:
# Given a list of numbers [12, 7, 9, 14, 21, 30, 5, 8], do the following:
#
# Create a new list containing only the even numbers.
# Create another new list containing only the odd numbers.

list_numbers = [12, 7, 9, 14, 21, 30, 5, 8]
even_numbers = []
odd_numbers = []
for num in range(len(list_numbers)):
    if list_numbers[num] % 2 == 0:
        even_numbers.append(list_numbers[num])
    elif list_numbers[num] % 2 != 0:
        odd_numbers.append(list_numbers[num])

print(even_numbers)
print(odd_numbers)


