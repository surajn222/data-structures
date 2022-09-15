# Recursive function to check if `s[low…high]` is a palindrome or not
def isPalindrome(s, low, high):
	return (low >= high) or (s[low] == s[high] and
							 isPalindrome(s, low + 1, high - 1))


# Function to check if a given string is a rotated palindrome or not
def isRotatedPalindrome(s):
	# length of the given string
	n = len(s)

	# check for all rotations of the given string if it
	# is palindrome or not
	for i in range(n):

		# in-place rotate the string by 1 unit
		s = s[1:] + s[0]

		# return true if the rotation is a palindrome
		if isPalindrome(s, 0, n - 1):
			return True

	# return false if no rotation is a palindrome
	return False


if __name__ == '__main__':

	# palindromic string
	s = 'ABCDCBA'

	# rotate it by 2 units
	s = s[2:] + s[:2]

	if isRotatedPalindrome(s):
		print('The string is a rotated palindrome')
	else:
		print('The string is not a rotated palindrome')


# ---------------------------------------------------------
# Expand in both directions of `low` and `high` to find
# palindrome of length `k`
def expand(s, low, high, k):
	while low >= 0 and high < len(s) and s[low] == s[high]:

		# return true palindrome of length `k` is found
		if high - low + 1 == k:
			return True

		# Expand in both directions
		low = low - 1
		high = high + 1

	# return false if palindrome of length `k` is not found
	return False


# Function to check if a palindromic substring of length `k` exists or not
def longestPalindromicSubstring(s, k):
	for i in range(len(s) - 1):
		# check if odd or even length palindrome of length `k`
		# having `s[i]` as its midpoint exists
		if expand(s, i, i, k) or expand(s, i, i + 1, k):
			return True

	return False


# Function to check if a given string is a rotated palindrome or not
def isRotatedPalindrome(s):
	# length of the given string
	n = len(s)

	# return true if the longest palindromic substring of length `n`
	# exists in the string `s + s`
	return longestPalindromicSubstring(s + s, n)


if __name__ == '__main__':

	# palindromic string
	s = 'ABCCBA'

	# rotate it by 2 units
	s = s[2:] + s[:2]

	if isRotatedPalindrome(s):
		print('The string is a rotated palindrome')
	else:
		print('The string is not a rotated palindrome')
