# Function to group elements of a given list based on the first
# occurrence of each element
def rearrange(A):
	# create an empty dictionary to store the frequency of each element
	# present in the input list
	freq = {}

	# traverse the input list and update the frequency of each element
	for i in A:
		freq[i] = freq.get(i, 0) + 1

	for i in A:
		# if `i` exists in the dictionary (first occurrence of `i`)
		if freq.get(i):
			# print `n` times, where `n = freq[i]`
			for _ in range(freq[i]):
				print(i, end=' ')

			# remove the element from the dictionary, so it would not
			# get processed again
			freq[i] = 0


if __name__ == '__main__':
	A = [5, 4, 5, 5, 3, 1, 2, 2, 4]
	rearrange(A)
