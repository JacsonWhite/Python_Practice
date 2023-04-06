# Countdown - Create a function that accepts a number as an input. 
# Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1,0]

# def new_list(num):
#     newer_list = []
#     for x in range(num, -1, -1):
#         newer_list.append(x)
#     return newer_list

# print(new_list(10))


# Print and Return - Create a function that will receive a list with two numbers. 
# Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2

# def new_list(num1):
#     print(num1[0])
#     return num1[1]

# print(new_list([4,5]))

# Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

# def adding_things(list1):
#     sum = 0
#     for x in range(0, len(list1), 1):
#         # print(list1[x])
#         sum = list1[0] + len(list1)
#     return sum

# print(adding_things([3,8,9,10,5]))



# Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value.
#  Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

# def this_list(list1):
#     if len(list1) < 2:
#         return False
#     new_list = []
#     count = 0
#     for x in range(0, len(list1)):
#         if list1[x] > list1[1]:
#             new_list.append(list1[x])
#             count += 1
#     print(count)
#     return new_list

# print(this_list([5,1,9,14,3,2,1,4,20]))
# print(this_list([3]))

# def int_str(input):
#     new_str =''
#     for i in input:
#         if i.isdigit():
#             new_str += i
#     return new_str
# print(int_str("0s1a3y5w7h9a2t4?"))    
