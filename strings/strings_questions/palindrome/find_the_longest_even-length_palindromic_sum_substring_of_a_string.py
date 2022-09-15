# Function to find the maximum length of a substring with an equal sum
# of left and right half
def longestPalindrome(s):
	# `total[i]` stores sum of digits of a substring `s[0…i-1]`
	total = [0] * (len(s) + 1)

	for i in range(1, len(s) + 1):
		total[i] = total[i - 1] + int(s[i - 1])

	# stores the maximum length of a substring with an equal sum
	# of left and right half
	max = 0

	# consider even length substring from index `i` to `j`
	for i in range(len(s) - 1):
		for j in range(i + 1, len(s), 2):
			# calculate the length of the substring
			length = j - i + 1

			# find the middle index of the substring
			mid = i + length // 2

			# if the sum of the left and right half is the same as the length of
			# the substring is more than the maximum length found so far
			if total[mid] - total[i] == total[j + 1] - total[mid] and max < length:
				max = length

	return max


if __name__ == '__main__':
	s = '13267224'
	print('The length of the longest palindromic sum substring is',
		  longestPalindrome(s))
