# Concatenate Two Lists in One List Item Wise
# Implement a function which takes two lists
# as parameter and return concatenation of these lists item wise.
#
# Example
#
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# concatenate(list1, list2)

def concat(list1, list2):
    new_list = []
    for each in range(len(list1)):
        new_list.append([list1[each], list2[each]])

    return new_list


result = concat(["Hello ", "take "], ["Dear", "Sir"])
print(result)
