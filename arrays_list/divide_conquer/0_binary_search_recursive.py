# Returns index of x in arr if present, else -1
# Array, low, high, element to be searched

# 1. Define the function and recursive function
# 2. Define the arguments for the function (arr, low, high, some element)
# 3. Define the base function or the return call (if clause on when to stop)
# 4. Define the if clauses (Any other clauses on when to call the function again)
# 5. Call the function

def binary_search(arr, low, high, x):
	# Check base case
	if high >= low:

		tab_str_low = ""
		for i in range(low): tab_str_low = tab_str_low + "_"

		# tab_str_low = [tab_str_low + "_" for _ in range(low)]

		tab_str_diff = ""
		for i in range(high - low - 1): tab_str_diff = tab_str_diff + "_"

		mid = (high + low) // 2

		print("Searching for array with indexes " + str(tab_str_low) + str(low) + tab_str_diff + str(
			high) + " where mid = " + str(mid))

		# If element is present at the middle itself
		if arr[mid] == x:
			return mid

		# If element is smaller than mid, then it can only
		# be present in left subarray
		elif arr[mid] > x:
			return binary_search(arr, low, mid - 1, x)

		# Else the element can only be present in right subarray
		else:
			return binary_search(arr, mid + 1, high, x)

	else:
		# Element is not present in the array
		return -1


# Test array
arr = [2, 3, 4, 10, 40, 50, 60, 70, 80, 81, 82, 83, 84, 85, 86, 90, 91, 92]
x = 4

# Function call
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
