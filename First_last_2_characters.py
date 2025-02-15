# First and Last 2 Characters
# Implement a function which takes a string as a
# parameter and returns new string which is made of
# the first 2 and the last 2 chars from a given a string.
# If the length of given string is less than 2 then return empty string.
#
# Example
#
# first_last_characters('appmillers')

def first_last_characters(word):
    word[0:3] + word[-2:]
    if len(word) < 2:
        return "word characters is less than 2"
    return word[0:3] + word[-2:]


result = first_last_characters("a")
print(result)

