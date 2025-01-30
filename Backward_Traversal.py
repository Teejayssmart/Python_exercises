# Write a while loop that starts at the last character
# in the string and works its way backwards to the first
# character in the string, printing each letter on a
# separate line, except backwards.

user_input = input("Enter a string: ")

index = len(user_input)-1  #starts from last character

while index >= 0:
    result = user_input[index]
    print(result)
    index -= 1

user_input = input("Enter a string: ")
index = 0  # starts from first character
while index < len(user_input):
    result = user_input[index]
    print(result)
    index += 1