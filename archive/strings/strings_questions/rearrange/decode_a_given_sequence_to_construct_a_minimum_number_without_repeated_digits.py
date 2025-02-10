from collections import deque


# Function to decode the given sequence to construct a minimum number
# without repeated digits
def decode(seq):
	# base case
	if not seq or not len(seq):
		return seq

	# `result` store the output string
	result = ''

	# create an empty stack of integers
	stack = deque()

	# run `n+1` times, where `n` is the length of the input sequence
	for i in range(len(seq) + 1):

		# push number `i+1` into the stack
		stack.append(i + 1)

		# if all characters of the input sequence are processed, or
		# the current character is 'I' (increasing)
		if i == len(seq) or seq[i] == 'I':
			# run till stack is empty
			while stack:
				# remove a top element from the stack and add it to the solution
				result += str(stack.pop())

	return result


if __name__ == '__main__':
	seq = 'IDIDII'  # input sequence

	print('The minimum number is', decode(seq))
