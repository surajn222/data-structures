# https://www.techiedelight.com/determine-given-string-is-palindrome-not/
# print(i)  # Operation
# i = i + 1  # Increment
# if i == 10:  # End/Break
# 	return
# fun_print(i)  # Call the function again

def isPalindrome(s, low, high):  # Init
	print(str(s[low]) + str(s[high]))

	if s[low] != s[high]:
		return False

	low = low + 1
	high = high - 1

	if low < high:
		isPalindrome(s, low, high)  # Call the function again

	return True


def for_loop_pal(s):
	for i in range(len(s)):
		if s[i] != s[len(s) - 1]:
			return False
		return True


if __name__ == '__main__':

	s = 'XYBYBYX'
	s = 'ABCDDCBA'

	if for_loop_pal(s):
		print('Palindrome')
	else:
		print('Not Palindrome')

	if isPalindrome(s, 0, len(s) - 1):
		print('Palindrome')
	else:
		print('Not Palindrome')
