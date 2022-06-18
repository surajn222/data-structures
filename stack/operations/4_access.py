#create a stack of nubers
stack_numbers = [10, 20, 14]
print(stack_numbers)

#value at index
value_at_index_0 = stack_numbers[0]
print(value_at_index_0)

#value at last index
value_at_index_last = stack_numbers[-1]
print(value_at_index_last)

#access all values
for index in range(len(stack_numbers)):
    print(stack_numbers[index])

#access all values
for element in stack_numbers:
    print(element)

#Definition
stack_numbers = [10, 20, 14, 30, 40, 50, 60]
print(stack_numbers)

#stack from index one to index three
stack_from_index_one_to_index_four = stack_numbers[1:4] #Read as one to three
print(stack_from_index_one_to_index_four)

#stack from index one to index three
stack_from_index_zero_to_index_four = stack_numbers[:4] #Read as zero to three
print(stack_from_index_zero_to_index_four)

#stack from index one to index three
stack_from_index_zero_to_index_last = stack_numbers[-3:-1] #Read as zero to three
print(stack_from_index_zero_to_index_last)