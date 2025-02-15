# Create a function which takes as parameter
# integer number (n) and based on this number
# it prints the following start pattern using
# nested loop and string formatting. So if
# n equals 5 the maximum number of stars
# (*) will be 5 in the pattern.

def print_pattern(n):
    for num in range(0, n):
        for num1 in range(0, num + 1):
            print("*", end=' ')
        print()

    for num in range(n, 0, -1):
        for num1 in range(0, num - 1):
            print("*", end=' ')
        print()

print_pattern(5)
