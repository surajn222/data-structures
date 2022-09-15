# https://www.techiedelight.com/introduction-pattern-matching/
# Function to find all occurrences of a pattern of length `m`
# in a given text of length `n`
def find(text, pattern):
	n = len(text)
	m = len(pattern)

	# base case 1: text is empty
	if not pattern:
		print('The pattern occurs with shift 0')
		return

	# base case 2: text is None, or text length is less than that of pattern
	if not text or len(pattern) > len(text):
		print('Pattern not found')
		return

	i = 0
	while i <= n - m:
		for j in range(m):
			if text[i + j] is not pattern[j]:
				break
			if j == m - 1:
				print('Pattern occurs with shift', i)
		i = i + 1


if __name__ == '__main__':
	text = 'ABCABAABCABAC'
	pattern = 'CAB'

	find(text, pattern)
