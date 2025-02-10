# https://www.techiedelight.com/reverse-string-python/
if __name__ == '__main__':
	input = "Reverse me"

	rev = input[::-1]
	print(rev)  # em esreveR

if __name__ == '__main__':
	input = "Reverse me"

	rev = ''.join(reversed(input))
	print(rev)  # em esreveR


def reverse(input):
	if len(input) <= 1:
		return input

	return reverse(input[1:]) + input[0]


if __name__ == '__main__':
	input = "Reverse me"

	rev = reverse(input)
	print(rev)  # em esreveR
