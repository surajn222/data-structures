# Function to remove all adjacent duplicates from the given string
def removeAdjDup(s):
	chars = list(s)
	n = len(s)

	# `k` maintains the index of the next free location in the result
	k = 0

	# `i` maintains the current index of the string
	i = 1

	# start from the second character
	while i < n:
		# if the current character is not the same as the
		# previous character, add it to the result
		if chars[i - 1] != chars[i]:
			chars[k] = chars[i - 1]
			k = k + 1
		else:
			# remove adjacent duplicates
			while i < len(chars) and chars[i - 1] == chars[i]:
				i = i + 1
		i = i + 1

	# add the last character to the result
	chars[k] = chars[i - 1]
	k = k + 1

	# construct a string with the first `k` chars
	s = ''.join(chars[:k])

	# start again if any duplicate is removed
	if k != n:
		return removeAdjDup(s)  # Schlemiel painter’s algorithm

	# if the algorithm didn't change the input string, that means
	# all the adjacent duplicates are removed
	return s


if __name__ == '__main__':
	s = 'DBAABDAB'
	print('The string left after removal of all adjacent duplicates is',
		  removeAdjDup(s))
