# Selection Sort
# for number of elements in the array
#  index = assume first element is minimal
#  for all elements in array
#    compare with index and find minimal element
#  swap it with index

print("Selection sort")
# Similar to bubble sort, except this algo uses index instead of elements to compare.

#Step 1
#In order to understand bubble sort, understand the inner loop first
array_arr = [10,8,6,4,2]

#This is inner loop.
#Just find the minimum value
#Assume minimum value is at index 0, find the minimum value
minimum_element_index = 0
for inner_loop_index in range(len(array_arr)):
    if array_arr[inner_loop_index] < array_arr[minimum_element_index]:
        minimum_element_index = inner_loop_index
    print(minimum_element_index)


#This is the entire program
for outer_loop_index in range(len(array_arr)):
    minimum_element_index = outer_loop_index
    for inner_loop_index in range(outer_loop_index, len(array_arr)):
        if array_arr[inner_loop_index] < array_arr[minimum_element_index]:
            minimum_element_index = inner_loop_index
        #print(minimum_element_index)
    array_arr[minimum_element_index], array_arr[outer_loop_index] = array_arr[outer_loop_index], array_arr[minimum_element_index]

print(array_arr)

#Worst case time complexity is n^2, because of two loops