# Determine if the first string can be transformed into the
# second string with a single edit operation
def checkEditDistance(first, second):
	# store length of both strings
	m = len(first)
	n = len(second)

	# difference between the length of both strings is more than one
	if abs(m - n) > 1:
		return False

	# to keep track of the total number of edits
	edits = 0

	# `i` and `j` keep track of the index of current characters in the
	# first and second strings, respectively
	i = j = 0

	# loop till either string runs out
	while i < m and j < n:

		# if the current character of both strings doesn't match
		if first[i] != second[j]:

			# when the length of the first string is more than the length
			# of the second string, remove the current character at
			# index `i` in the first string

			if m > n:
				i = i + 1

			# when the length of the first string is less than the length
			# of the second string, add the current character at index `j`
			# in the second string to the first string

			elif m < n:
				j = j + 1

			# when the length of both strings is the same, replace the character
			# present at index `i` in the first string with the character present
			# at index `j` in the second string.

			else:
				i = i + 1
				j = j + 1

			# increment the number of edits
			edits = edits + 1

		# if the current character of both strings matches
		else:
			i = i + 1
			j = j + 1

	# remove any extra characters left in the first string
	if i < m:
		edits = edits + 1

	# add any extra characters left in the second string at the end of the first string
	if j < n:
		edits = edits + 1

	# return true if the number of edits is exactly one return, false otherwise
	return edits == 1


if __name__ == '__main__':
	print(checkEditDistance("xyz", "xz"))  # True
	print(checkEditDistance("xyz", "xyyz"))  # True
	print(checkEditDistance("xyz", "xyx"))  # True
	print(checkEditDistance("xyz", "xxx"))  # False

# PSEUDOCODE
# Comparing xyz to xz
# Compare x to x
# Compare y to x. if not same, increment the index of xyz. edits++
# Compare z to z

# Comparing xyz to xyyz
# Compare x to x
# Compare y to y.
# Compare z to y. if not same, increment the index of xyyz. edits++
# Compare z to z
