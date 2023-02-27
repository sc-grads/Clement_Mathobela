# def equilibrium_index(my_list):
#     for x in range(0,len(my_list)):
#         if sum(my_list[:x]) == sum(my_list[x+1:]):
#             return x
#
#     return False
#
# nums = [2, 3, 10, 5]
# print(equilibrium_index(nums))  # => 2
#
# nums = [3, 3, 10, 5]
# print(equilibrium_index(nums))  # => False