#create a list of nubers
list_numbers = [10, 20, 14]
print(list_numbers)

#access all values
for index in range(len(list_numbers)):
    print(list_numbers[index])

#access all values
for element in list_numbers:
    print(element)



# definition
list_numbers = [10, 20, 14, 30, 40, 50, 60]
print(list_numbers)

# accessing subarrays
# list from index one to index three
list_from_index_one_to_index_four = list_numbers[1:4] #Read as one to three
print(list_from_index_one_to_index_four)

# list from index one to index three
list_from_index_zero_to_index_four = list_numbers[:4] #Read as zero to three
print(list_from_index_zero_to_index_four)

# list from index one to index three
list_from_index_zero_to_index_last = list_numbers[-3:-1] #Read as zero to three
print(list_from_index_zero_to_index_last)
