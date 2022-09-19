# Determine if characters of a given word follow specific order as
# defined by characters of the given pattern
def checkPattern(word, pattern):
	# invalid input
	if not word or not pattern or len(word) < len(pattern):
		return False

	# stores previous character
	prev = None

	# loop through all chars of the pattern
	for curr in pattern:

		# return false if the last occurrence of the previous character is after
		# the first occurrence of the current character in the input word

		firstIndex = word.find(curr)
		if firstIndex == -1 or (prev and word.rfind(prev) > firstIndex):
			return False

		# set current as previous for the next iteration
		prev = curr

	# we reach here if the given word matches the pattern
	return True


if __name__ == '__main__':

	word = 'Techie Delight'
	pattern = 'el'

	if checkPattern(word, pattern):
		print('Pattern found')
	else:
		print('Pattern not found')
