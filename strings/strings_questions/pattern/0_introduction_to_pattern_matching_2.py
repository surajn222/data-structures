# https://www.techiedelight.com/introduction-pattern-matching/
# Function to find all occurrences of a pattern of length `m`
# in a given text of length `n`
def find_method_1(text, pattern):
	len_text = len(text)
	len_pattern = len(pattern)

	# text = 'ABCABAABCABAC'
	# pattern = 'CABAC'

	# Start checking from index 1 in text
	# Match pattern with index
	# Print if match
	# Move ahead

	for i in range(len_text):
		# print(text[i])
		if (text[i:i + len_pattern] == pattern):
			print("at index: " + str(i))
			print(pattern)


def find_method_2(text, pattern):
	len_text = len(text)
	len_pattern = len(pattern)

	# text = 'ABCABAABCABAC'
	# pattern = 'CABAC'

	# Start checking from index 1 in text
	# Start checking from index 1 in pattern
	# if first index in both do not match, break and move on to the next index in text
	# if all chars match, break will not happen and index can be printed

	for index_text in range(len_text - len_pattern):
		for index_pattern in range(len(pattern)):
			if text[index_text] != pattern[index_pattern]:
				break
			print("At index: " + str(index_text) + ": " + str(text[index_text:index_text + len_pattern]))


def find_method_3(text, pattern):
	len_text = len(text)
	len_pattern = len(pattern)

	# base case 1: text is empty
	if not pattern:
		print('The pattern occurs with shift 0')
		return

	# base case 2: text is None, or text length is less than that of pattern
	if not text or len(pattern) > len(text):
		print('Pattern not found')
		return

	# PATTERN in TEXT
	# text = 'ABCABAABCABAC'
	# pattern = 'CAB'

	# Logic =
	# cab = abc (text 0-3)
	# cab = bca (text 1-4)
	# cab = cab (text 2-5)
	# cab = aba (text 3-6)
	# .....

	# One way to solve this problem is
	# 1. Start from index_1 of text == index_1 of patter.
	# case1:
	#	if does not match, break and move to index_2 of text == index_2 of pattern
	# 	if does not match, break and move
	# case2:
	# 	if it does match, then
	#		just  (the size of the number of matches) == (size of pattern)

	i = 0
	while i <= n - m:
		for j in range(m):
			print("j = " + str(j))
			if text[i + j] is not pattern[j]:
				print("text " + str(i) + " " + str(j) + " is not " + " pattern " + str(j))
				print(str(text[i + j]) + " is not " + str(pattern[j]))
				break
			if j == m - 1:
				print(str(j) + " is equal to " + str(m - 1))
				print('Pattern occurs with shift', i)

		i = i + 1


if __name__ == '__main__':
	text = 'ABCABAABCABAC'
	pattern = 'CABAC'

	find_method_1(text, pattern)
	find_method_2(text, pattern)
# find_method_3(text, pattern)
