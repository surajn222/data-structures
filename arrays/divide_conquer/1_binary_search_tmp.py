# 1. Define the function and recursive function
# 2. Define the arguments
# 3. Define the base function
# 4. Define the if clauses
# 5. Call the funtion

# Sorted rotated array
def binary_search(arr, low, high):
	if high >= low:
		mid = (high + low) // 2
		print("High low index: " + str(low) + ", " + str(mid) + ", " + str(high))
		high_element = arr[high]
		low_element = arr[low]
		mid_element = arr[mid]
		left_immediate_element = arr[mid - 1]
		right_immediate_element = arr[mid + 1]
		print("High low elements: " + str(left_immediate_element) + ", " + str(mid_element) + ", " + str(
			right_immediate_element))
		if left_immediate_element >= mid_element and mid_element <= right_immediate_element:
			return mid

		if mid_element <= low_element:
			return binary_search(arr, low, mid - 1)
		elif mid_element >= low_element:
			return binary_search(arr, mid + 1, high)
	else:
		return -1


arr = [2, 3, 4, 5, 6, 7, 0, 1]
# arr = [6,7,0,1,2,3,4,5]
arr = [1, 2, 3]  # Corner case
x = 3
index = binary_search(arr, 0, len(arr) - 1)
print(index)
