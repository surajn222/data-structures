# Insertion sort
# for len(array)
# 1: for 2 - len(array): find the minimal element and swap
# 2: for 3 - len(array): find the minimal element and swap
# 3: for 4 - len(array): find the minimal element and swap
# 4: for 5 - len(array): find the minimal element and swap


print("Insertion sort")

#Step 1
#In order to understand bubble sort, understand the inner loop first
array_arr = [3,4,10,8,4]

#This is inner loop.
# This loop will push the only biggest element to the end of the array.
#Lets try to fix one element - array_arr[3] = 8
current_element_to_be_rearranged_index = 3
current_element_to_be_rearranged_value = array_arr[current_element_to_be_rearranged_index]
inner_loop_index = current_element_to_be_rearranged_index - 1

while inner_loop_index > 0 and current_element_to_be_rearranged_value < array_arr[inner_loop_index]:
    print("Current element " + str(current_element_to_be_rearranged_value))
    print("Element from the array j " + str(array_arr[inner_loop_index]))
    array_arr[inner_loop_index + 1] = array_arr[inner_loop_index]
    inner_loop_index=inner_loop_index - 1

print("Start")

#This is the entire program
array_arr = [10,8,6,4,2]

for outer_loop_index in range(1, len(array_arr)):
    current_element_to_be_rearranged_index = outer_loop_index
    current_element_to_be_rearranged_value = array_arr[current_element_to_be_rearranged_index]
    inner_loop_index = current_element_to_be_rearranged_index - 1

    while inner_loop_index >= 0 and current_element_to_be_rearranged_value < array_arr[inner_loop_index]:
        print("Current element " + str(current_element_to_be_rearranged_value))
        print("Element to be compared j " + str(array_arr[inner_loop_index]))
        #array_arr[inner_loop_index + 1], array_arr[inner_loop_index] = array_arr[inner_loop_index], array_arr[inner_loop_index + 1]
        array_arr[inner_loop_index + 1] = array_arr[inner_loop_index]
        inner_loop_index = inner_loop_index - 1
    array_arr[inner_loop_index + 1] = current_element_to_be_rearranged_value
    print(array_arr)



#Worst case time complexity is n^2, because of two loops