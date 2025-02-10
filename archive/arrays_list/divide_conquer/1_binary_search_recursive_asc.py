# Returns index of x in arr if present, else -1
# Array, low, high, element to be searched

# 1. Define the function and recursive function
# 2. Define the arguments for the function
# 3. Define the base function or the return call
# 4. Define the if clauses
# 5. Call the function

def binary_search(arr, low, high, x):
	# Check base case
	if high >= low:
		# high = 0, low = 0
		# high = 1, low = 3
		# high = 5, low = 8
		# high = 2, low = 1

		mid = (high + low) // 2
		# high = 0, low = 0, mid = 0
		# high = 1, low = 3, mid = 2
		# high = 5, low = 8, mid = 6
		# high = 2, low = 1, mid = 1

		# If element is present at the middle itself
		if arr[mid] == x:
			# arr[mid] = 4, x = 4
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			# arr[mid] = 4, x = 3
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			# arr[mid] = 4, x = 6
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
