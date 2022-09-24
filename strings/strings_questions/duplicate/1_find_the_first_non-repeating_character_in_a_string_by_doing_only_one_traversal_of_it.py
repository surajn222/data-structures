# Function to find the first non-repeating character in
# the string by doing only a single traversal of it

# PSEUDOLOGIC
# Logic
# s = 'ABCDBAGHC'
# Step1:
# dictionary with count and index: {'A': (2, 5), 'B': (2, 4), 'C': (2, 8), 'D': (1, 3), 'G': (1, 6), 'H': (1, 7)}
# Step2:
# Then loop through the dict, and find the char with count 1, and least index

def findNonRepeatingChar(s):
	# base case
	if not s:
		return -1

	# dictionary to store character count and the index of its
	# last occurrence in the string
	d = {}

	for index, char in enumerate(s):
		frequency, prevIndex = d.get(char, (0, index))
		d[char] = (frequency + 1, index)

	print(d)

	# stores index of the first non-repeating character
	min_index = -1

	# Traverse the dictionary and find a character with count 1 and
	# a minimum index of the string
	for key, values in d.items():
		count, firstIndex = values
		if count == 1 and (min_index == -1 or firstIndex < min_index):
			min_index = firstIndex

	return min_index


if __name__ == '__main__':

	s = 'ABCDBAGHC'

	index = findNonRepeatingChar(s)
	if index != -1:
		print('The first non-repeating character in the string is', s[index])
	else:
		print('The string has no non-repeating character')

# TAKEAWAYS
# 1. Enumerate function in python for list
# for index, char in enumerate(list):
# 	print(index, char)
# 2. Dictionary with char and tuple
# for index, char in enumerate(s):
# 	frequency, prevIndex = d.get(char, (0, index))
# 	d[char] = (frequency + 1, index)
# 4.
# 5.
