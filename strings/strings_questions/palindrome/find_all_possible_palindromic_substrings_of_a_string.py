# Expand in both directions of `low` and `high` to find all palindromes
def expand(s, low, high, palindromes):
	print("low = " + str(low))
	print("high = " + str(high))
	# run till `s[low.high]` is not a palindrome
	while low >= 0 and high < len(s) and s[low] == s[high]:
		# push all palindromes into a set
		print("Palindrome: " + str(s[low: high + 1]))
		palindromes.add(s[low: high + 1])

		# Expand in both directions
		low = low - 1
		high = high + 1


# Function to find all unique palindromic substrings of a given string
def findPalindromicSubstrings(s):
	# create an empty set to store all unique palindromic substrings
	palindromes = set()

	for i in range(len(s)):
		# find all odd length palindrome with `s[i]` as a midpoint
		print("expand i - odd length")
		expand(s, i, i, palindromes)
		print("\n")
		# find all even length palindrome with `s[i]` and `s[i+1]`
		# as its midpoints
		print("expand i + 1 - even length")
		expand(s, i, i + 1, palindromes)
		print("\n\n")

	# print all unique palindromic substrings
	print(palindromes, end='')


if __name__ == '__main__':
	s = 'google'
	findPalindromicSubstrings(s)

# PSEUDOCODE
# Given a string, lets say 'google'
# Find all palindromes around g, o, o, g, l, e
# Find all palindromes around go, oo, og, gl, le
# Way to find palindrome around a character:
# 1. Check index left = right
# 2. Move left to left, and right to right
# 3. check if chars match
# 4. Repeat
