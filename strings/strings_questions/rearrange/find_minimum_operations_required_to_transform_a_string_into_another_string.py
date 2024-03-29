import collections


# Function to find the minimum number of operations required to transform a given
# into another string
def getMinimumOperations(first, second):
	# to keep track of the minimum number of operations required
	count = 0

	# `i` and `j` keep track of the current characters' index in the
	# first and second strings, respectively

	# start from the end of the first and second string
	i = len(first) - 1
	j = i

	while i >= 0:
		# if the current character of both strings doesn't match,
		# search for `second[j]` in substring `first[0,i-1]` and
		# increment the count for every move
		while i >= 0 and first[i] != second[j]:
			print("i: " + str(i) + " j: " + str(j))
			i = i - 1
			count = count + 1

		i = i - 1
		j = j - 1

	# return the minimum operations required
	return count


# Function to determine if the first string can be transformed into
# the second string
def isTransformable(first, second):
	# if the length of both strings differs
	if len(first) != len(second):
		return False

	# return true if both strings have the same set of characters
	return collections.Counter(first) == collections.Counter(second)


if __name__ == '__main__':

	first = 'ADCB'
	second = 'ABCD'

	if isTransformable(list(first), list(second)):
		print('The minimum operations required to convert the String', first,
			  'to string', second, 'are', getMinimumOperations(first, second))
	else:
		print('The string cannot be transformed')

# TAKEAWAY
# 2. To find the minimum number of operations required to convert the first string to the second string, the idea is to simultaneously traverse both strings from the end. If the last characters of both strings match, move to the next pair of characters. If the last character of both strings doesn’t match, find the index of the matching character in the first string. The difference between both indices represents the number of characters in the first string that has to be moved before the current character of the first string.
