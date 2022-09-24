# Function to remove characters from a word that are not present in
# the specified pattern
def removeChars(word, allowed):
	allow = set(allowed)
	return list(filter(lambda x: x in allow, word))


# Function to remove adjacent duplicates characters from a word
def removeDuplicates(chars):
	prev = None
	k = 0

	for i in range(len(chars)):
		if prev != chars[i]:
			chars[k] = chars[i]
			k = k + 1
			prev = chars[i]

	return ''.join(chars[:k])


# Determine if characters of a given word follow specific order as
# defined by characters of the given pattern
def checkPattern(word, pattern):
	# invalid input
	if not word or not pattern:
		return False

	return removeDuplicates(removeChars(word, pattern)) == pattern


if __name__ == '__main__':

	word = 'Techie Delight'
	pattern = 'el'

	if checkPattern(word, pattern):
		print('Pattern found')
	else:
		print('Pattern not found')

# TAKEAWAY
# 1. Remove characters - Given pattern, word, only chars from pattern should remain in word
# 2. Remove duplicates - Given a str, remove adjacent duplicates
