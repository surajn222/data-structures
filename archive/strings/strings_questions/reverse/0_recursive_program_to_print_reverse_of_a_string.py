# https://www.techiedelight.com/recursive-program-to-print-reverse-of-a-given-string/
# Recursive function to print reverse of a given string
def reverse(s, k):
	# base case: end of the string is reached
	if k == len(s):
		print("returning now")
		return

	# recur for the next character
	reverse(s, k + 1)

	# print current character
	print(s[k])


if __name__ == '__main__':
	s = 'Techie Delight'
	print('Reverse of the given string is', end=' ')
	reverse(s, 0)
