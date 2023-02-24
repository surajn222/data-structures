# Complex
def rearrange(self, arr, n):
	temp = n // 2
	mx = arr[n - 1] + 1

	for i in range(temp): arr[i] = mx * arr[n - 1 - i] + arr[i]

	lst = n - 1
	if n % 2: arr[lst], lst = arr[temp], lst - 1

	for j in range(temp):
		i = temp - j - 1
		arr[lst], arr[lst - 1] = arr[i] % mx, arr[i] // mx
		lst = lst - 2

	return


# Given a sorted array of positive integers, rearrange the array alternately i.e first element should be maximum value, second minimum value, third second max, fourth second min and so on.

# Python program to rearrange an array in minimum maximum form

# Prints max at first position, min at second position
# second max at third position, second min at fourth
# position and so on.

# https://leetcode.com/problems/rearrange-array-elements-by-sign/ #Pending

def rearrange(arr, n):
	# Auxiliary array to hold modified array
	list_temp = n * [None]

	# Indexes of smallest and largest elements from remaining array.
	index_small = 0
	index_large = n - 1

	# To indicate whether we need to copy remaining
	# largest or remaining smallest at next position
	flag = True

	# Store result in list_temp[]
	for i in range(n):
		if flag is True:
			# start at the end of the list, and reduce one index at a time
			list_temp[i] = arr[index_large]
			index_large -= 1
		else:
			# start at the beginning of the list, and increase one index at a time
			list_temp[i] = arr[index_small]
			index_small += 1

		flag = bool(1 - flag)

	arr = list_temp.copy()
	# OR arr = list_temp[:]

	return arr


# driver code
arr = [1, 2, 3, 4, 5, 6]
length_of_array = len(arr)
print("original array")
print(arr)
print("modified array")
print(rearrange(arr, length_of_array))

# https://www.geeksforgeeks.org/rearrange-array-maximum-minimum-form-set-2-o1-extra-space/
