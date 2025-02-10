# TODO: Completed
# function to find the once
# appearing element in array

# 10 ^ 5 = 15
# 15 ^ 5 = 10
# https://leetcode.com/problems/single-number-ii/ #Pending
# https://leetcode.com/problems/single-number-iii/ #Pending #Hashing
def findSingle(ar, n):
	res = ar[0]
	print("starting element: " + str(res))

	# Do XOR of all elements and return
	for i in range(1, n):
		print(str(res) + " ^ " + str(ar[i]))
		res = res ^ ar[i]
		print(res)
	return res

# Driver code
ar = [2, 3, 5, 4, 5, 3, 4]
print("Element occurring once is", findSingle(ar, len(ar)))
ar = [0, 0, 4, 1, 1, 8, 8]
print("Element occurring once is", findSingle(ar, len(ar)))

# This code is contributed by __Devesh Agrawal__