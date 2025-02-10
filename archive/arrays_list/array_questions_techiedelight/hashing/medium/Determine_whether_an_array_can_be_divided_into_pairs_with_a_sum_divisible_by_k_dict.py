# Determine if an array can be divided into pairs such that the sum of elements
# in each pair is divisible by the given integer `k`

# We can improve the time complexity to O(n) using hashing.
# reate a map to keep track of remainders of all input elements with k, i.e.,
# map = remainder, the frequency of the remainder.
#
# For elements     directly divisible by k, the remainder r would be 0, and the frequency should be even.
# For elements not directly divisible by k and having remainder r,
# 		A pair only exists when there is another array element with remainder k-r.
# 		Therefore, the frequency of the remainder r must be equal to the frequency of k-r.

# For eg:
# (6,6)
# Remainders (0, 0): Pair can be formed

# (9,6)
# Remainders: (3, 0): Pair cannot be formed

# (6,6,9,15,9,15)
# Remainders: (0,0,3,3,3,3)

# (6,6,2,2)
# Remainders: (0,0,2,2)

def findPairs(arr, k):
	# base case: input contains an odd number of elements
	# (an odd number of elements cannot be paired)
	if len(arr) & 1:
		return False

	# create a count array to keep track of the remainder of input elements with `k`
	# freq = [0] * k
	freq = {}

	# consider each element
	for i in range(len(arr)):
		# calculate the remainder of the current element with `k`
		print("index: " + str(i))
		print("value: " + str(arr[i]))
		print("k: " + str(k))
		r = arr[i] % k

		print("remainder: " + str(r))

		# increment the count array
		# freq[r] += 1
		freq[r] = freq.get(r, 0) + 1

		print(freq)

	# the frequency of elements directly divisible by `k` must be even
	if freq.get(0, 0) % 2 != 0:
		return False

	# for each element with remainder `r`, there should be an element with
	# remainder `k-r`
	for r in range(1, k // 2 + 1):
		if freq.get(r, 0) != freq.get(k - r, 0):
			return False

	# we reach here only when each element forms a pair
	return True


if __name__ == '__main__':

	arr = [2, 9, 4, 1, 3, 5]
	arr = [6, 6, 9, 15, 9, 15, 7, 5]
	k = 6

	if findPairs(arr, k):
		print("Pairs can be formed")
	else:
		print("Pairs cannot be formed")
