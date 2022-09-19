# https://www.techiedelight.com/difference-between-subarray-subsequence-subset/
# Function to print all sublists of the specified list
def printallSublists(nums):
	# consider all sublists starting from i
	for i in range(len(nums)):
		# consider all sublists ending at `j`
		for j in range(i, len(nums)):
			# Function to print a sublist formed by [i, j]
			print(nums[i: j + 1])


if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5]
	printallSublists(nums)


# -----------------------------------------------------------
# Function to print all non-empty substrings of the specified string
def printAllSubstrings(s):
	# consider all substrings starting from i
	for i in range(len(s)):
		# consider all substrings ending at j
		for j in range(i, len(s)):
			print(s[i: j + 1], end=' ')


if __name__ == '__main__':
	s = 'techie'
	printAllSubstrings(s)


# -----------------------------------------------------------------

# Function to print all subsequences of the specified string
def findPowerSet(seq):
	# N stores the total number of subsets
	N = int(pow(2, len(seq)))

	# generate each subset one by one
	result = []
	for i in range(N):
		s = ''
		# check every bit of `i`
		for j in range(len(seq)):
			# if j'th bit of `i` is set, print S[j]
			if (i & (1 << j)) != 0:
				s += seq[j]
		result.append(s)
	print(result)


if __name__ == '__main__':
	seq = 'apple'
	findPowerSet(seq)
