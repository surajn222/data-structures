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
