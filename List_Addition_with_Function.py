# Implement a function which takes two parameters -
# a list and a value and returns new list with value
# inserted in it without modifying the original list.
#
# Example
#
# list1 = [1,2,3,4,5]
# list2 = custom_insert(list1, 6)
# print(list1)
# print(list2)

def muting_list(d_list, d_value):
    # to update a list without altering the original list

    # make a copy of list
    copy_list = d_list.copy()
    # add 6 to copied

    copy_list.append(d_value)
    # returned copied list
    print(d_list)
    return copy_list


print(muting_list([1, 2, 3, 4, 5], 6))

