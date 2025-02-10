# We can improve the time complexity to O(n) using hashing.
# The idea is to traverse the input array and create a map to keep track of remainders of all input elements with k, i.e.,
# map = remainder, the frequency of the remainder.
#
# For elements     directly divisible by k, the remainder r would be 0, and the frequency should be even.
# For elements not directly divisible by k and having remainder r,
# 		A pair only exists when there is another array element with remainder k-r.
# 		Therefore, the frequency of the remainder r must be equal to the frequency of k-r.

# Determine if an array can be divided into pairs such that the sum of elements
# in each pair is divisible by the given integer `k`
def findPairs(arr, k):
	# base case: input contains an odd number of elements
	# (an odd number of elements cannot be paired)
	if len(arr) & 1:
		return False

	# create a count array to keep track of the remainder of input elements with `k`
	freq = [0] * k

	# consider each element
	for i in range(len(arr)):
		# calculate the remainder of the current element with `k`
		print("index: " + str(i))
		print("value: " + str(arr[i]))
		print("k: " + str(k))
		r = arr[i] % k

		print("remainder: " + str(r))

		# increment the count array
		freq[r] += 1

		print(freq)

	# the frequency of elements directly divisible by `k` must be even
	if freq[0] % 2 != 0:
		return False

	# for each element with remainder `r`, there should be an element with
	# remainder `k-r`
	for r in range(1, k // 2 + 1):
		print("freq of " + str(r))
		print(freq[r])
		print(freq[k - r])
		if freq[r] != freq[k - r]:
			return False

	# we reach here only when each element forms a pair
	return True


if __name__ == '__main__':

	# arr = [2, 9, 4, 1, 3, 5]
	arr = [6, 6, 9, 15, 9, 15, 7, 5]
	k = 6

	if findPairs(arr, k):
		print("Pairs can be formed")
	else:
		print("Pairs cannot be formed")
