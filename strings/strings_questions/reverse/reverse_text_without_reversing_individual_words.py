from collections import deque


# Function to reverse a text without reversing the individual words
def reverseText(s):
	# base case
	if not s:
		return s

	# `s[low…high]` forms a word
	low = high = 0

	# create an empty stack
	stack = deque()

	# scan the text
	for i, c in enumerate(s):
		# if space is found, we found a word
		if c == ' ':
			# push each word into the stack
			stack.append(s[low:high + 1])

			# reset `low` and `high` for the next word
			low = high = i + 1
		else:
			high = i

	# push the last word into the stack
	stack.append(s[low:])

	# construct the string by following the LIFO order
	sb = ""
	while stack:
		sb += stack.pop() + ' '

	return sb[:-1]  # remove last space


if __name__ == '__main__':
	s = 'Preparation Interview Technical'
	print(reverseText(s))


# ---------------------------------------------------
# Utility function to swap the elements at positions `i` and `j` in the list
def swap(chars, i, j):
	temp = chars[i]
	chars[i] = chars[j]
	chars[j] = temp


# Utility function to reverse sublist `chars[begin…end]`
def reverseSublist(chars, begin, end):
	while begin < end:
		swap(chars, begin, end)
		begin = begin + 1
		end = end - 1


# Function to reverse a text without reversing the individual words.
def reverseText(s):
	# base case
	if not s:
		return s

	# since a string is immutable, convert it to a character list
	chars = list(s)

	# `chars[low…high]` forms a word
	low = high = 0

	# scan the text
	for i in range(len(chars)):

		# if space is found, we found a word
		if chars[i] == ' ':

			# reverse the found word
			reverseSublist(chars, low, high)

			# reset `low` and `high` for the next word
			low = high = i + 1

		else:
			high = i

	# reverse the last word
	reverseSublist(chars, low, high)

	# reverse the whole text
	reverseSublist(chars, 0, len(chars) - 1)

	return ''.join(chars)


if __name__ == '__main__':
	s = 'Preparation Interview Technical'
	print(reverseText(s))
