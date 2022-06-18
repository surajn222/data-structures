import sys

n = int(input("Enter the size of list : "))
print("\n")
# map_object = map(float, input().split())
# print(map_object)
list_nums = list(map(int,input().strip().split()))[:4]
print("User List: ", list_nums)
sys.exit()

argument_1_iterable = [2, 4, 6, 8, 10]
argument_2_iterable = [2,2,2,2,2]

#returns square of a number
def function_to_be_executed_on_the_following_arguments(argument_1_iterable, argument_2_iterable):
  return argument_1_iterable * argument_2_iterable

# apply square() function to each item of the numbers list
squared_numbers_iterator = map(function_to_be_executed_on_the_following_arguments, argument_1_iterable, argument_2_iterable)

print(squared_numbers_iterator)
print(type(squared_numbers_iterator))

# converting to list
squared_numbers = list(squared_numbers_iterator)
print(squared_numbers)

# Output: [4, 16, 36, 64, 100]