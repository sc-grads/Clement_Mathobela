# Consider the following string: nums = '10,20,30,40,50'
# Create a Python script that creates a list of integers from the string.
# The resulting list will be: [10, 20, 30, 40, 50]
nums = '10,20,30,40,50'
nums_list = nums.split(',')
nums_int = [int(i) for i in nums_list]
print(nums_int)
