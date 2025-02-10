# 1. Define the function and recursive function
# 2. Define the arguments
# 3. Define the base function
# 4. Define the if clauses
# 5. Call the funtion

def binary_search(arr, low, high, element_to_search):
	print("High low: " + str(high) + ", " + str(low))
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == element_to_search:
			return mid

		if arr[mid] > element_to_search:
			return binary_search(arr, low, mid - 1, element_to_search)
		else:
			return binary_search(arr, mid + 1, high, element_to_search)
	else:
		return -1


arr = [0, 1, 2, 3, 4, 5]

arr = [2, 3, 7, 9]
x = 3

index = binary_search(arr, 0, len(arr) - 1, 9)

print(index)
