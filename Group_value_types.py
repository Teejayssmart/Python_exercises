# Group Value Types
# Implement a function which takes a List a
# parameter and groups them according to their data types
# (integer or string) and return dictionary.
#
# Hint :
#
# Use isinstance() function to check data type.
#
# Use fromkeys() method to solve this challenge
#
# Example
#
# custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
# group_types(custom_list)


custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]


def group_value(p_list):
    new_dict = {}.fromkeys(p_list, 0)  # initialise an empty dictionary for both key , value
    for item in range(len(p_list)):  # loop through the list
        if isinstance(p_list[item], int): # if each item in each list is an int
            new_dict[p_list[item]] = "int"   # do this
        elif isinstance(p_list[item], str):   # if each item in each list is string
            new_dict[p_list[item]] = "string"  # do this

    return new_dict


result = group_value([10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50])

print(result)
