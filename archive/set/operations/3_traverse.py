#create a list of nubers
set_set_name = {1,2,3,4}
print(set_set_name)

#access all values
#Not possible in sets
# for index in range(len(set_set_name)):
#     print(set_set_name[index])

#access all values
for element in set_set_name:
    print(element)

for id,val in enumerate(set_set_name):
    print(id, val)

# accessing subarrays
# list from index one to index three
#Not possible in sets
# set_from_index_one_to_index_four = set_set_name[1:4] #Read as one to three
# print(set_from_index_one_to_index_four)


# list from index one to index three
#Not possible in sets
# set_from_index_zero_to_index_four = set_set_name[:4] #Read as zero to three
# print(set_from_index_zero_to_index_four)


# list from index one to index three
#Not possible in sets
# set_from_index_zero_to_index_last = set_set_name[-3:-1] #Read as zero to three
# print(set_from_index_zero_to_index_last)
