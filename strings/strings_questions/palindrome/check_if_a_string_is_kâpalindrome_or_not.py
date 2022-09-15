# Function to check if the given string is k–palindrome or not
def isKPalindrome(X, m, Y, n):
	# if either string is empty, remove all characters from the other string
	if m == 0 or n == 0:
		return n + m

	# ignore the last characters of both strings if they are the same
	# and recur for the remaining characters
	if X[m - 1] == Y[n - 1]:
		return isKPalindrome(X, m - 1, Y, n - 1)

	# if the last character of both strings is different

	# remove the last character from the first string and recur
	x = isKPalindrome(X, m - 1, Y, n)

	# remove the last character from the second string and recur
	y = isKPalindrome(X, m, Y, n - 1)

	# return one more than the minimum of the above two operations
	return 1 + min(x, y)


if __name__ == '__main__':

	s = 'CABCBC'
	k = 2

	# get reverse of s
	rev = s[::-1]

	if isKPalindrome(s, len(s), rev, len(s)) <= 2 * k:
		print('k-palindrome')
	else:
		print('Not a k–palindrome')
