print("Bubble sort")

# Step 1
# In order to understand bubble sort, understand the inner loop first
array_arr = [0, 8, 5, 2, 1]

# This is inner loop. This loop will push the only biggest element to the end of the array.
for int_inner_loop_index in range(len(array_arr) - 1):
	# Check if the current element in bigger than the next element. If it is, push to the right. Do this for every element
	if array_arr[int_inner_loop_index] > array_arr[int_inner_loop_index + 1]:
		# swap elements
		array_arr[int_inner_loop_index], array_arr[int_inner_loop_index + 1] = array_arr[int_inner_loop_index + 1], \
																			   array_arr[int_inner_loop_index]

# The above is the actual sorting operation

# Step 2
array_arr = [0, 8, 5, 2, 1]
# Now decorate the inner loop with an outer loop
for outer_loop_index in range(len(array_arr) - 1):
	for int_inner_loop_index in range(len(array_arr) - 1 - outer_loop_index):
		# Check if the current element in bigger than the next element. If it is, push to the end
		if array_arr[int_inner_loop_index] > array_arr[int_inner_loop_index + 1]:
			# swap elements
			array_arr[int_inner_loop_index], array_arr[int_inner_loop_index + 1] = array_arr[int_inner_loop_index + 1], \
																				   array_arr[int_inner_loop_index]

print(array_arr)

# Worst case time complexity: n^2, because two loops
