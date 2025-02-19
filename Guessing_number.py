#number guessing game

numbers = [4, 7, 2, 9, 5]
masked_list = ["_", "_", "_", "_", "_"]

#collect input from user
guess = int(input("Guess a number: "))

#loop through the numbers
for position in range(len(numbers)):
    #get number at the each position
    num = numbers[position]
    #compare guessed number with number at current position
    if guess == num: # if number matches, update
        masked_list[position] = num
print(masked_list)