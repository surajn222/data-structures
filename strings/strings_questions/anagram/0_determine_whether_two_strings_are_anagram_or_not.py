# Function to check if `X` and `Y` are anagrams or not
def isAnagram_1(word1, word2):
	# if X's length is not the same as Y's, they can't be an anagram
	if len(word1) != len(word2):
		return False

	# create an empty dictionary
	freq = {}

	# maintain the count of each character of `X` in the dictionary
	for i in range(len(word1)):
		freq[word1[i]] = freq.get(word1[i], 0) + 1

	# do for each character `y` of `Y`
	for i in range(len(word2)):

		# if `y` is found not in the dictionary, i.e., either `y` is not present
		# in string `X` or has more occurrences in string `Y`
		if not word2[i] in freq:
			return False

		# decrease the frequency of `y` on the dictionary
		freq[word2[i]] = freq[word2[i]] - 1

		# if its frequency becomes 0, erase it from the dictionary
		if freq[word2[i]] == 0:
			del freq[word2[i]]

	# return true if the dictionary becomes empty
	return not freq


def isAnagram_2(word1, word2):
	# Create two dictionaries with frequency of chars and match them
	if len(word1) != len(word2):
		return False

	# create an empty dictionary
	freq = {}
	freq_2 = {}

	# maintain the count of each character of `X` in the dictionary
	for i in range(len(word1)):
		freq[word1[i]] = freq.get(word1[i], 0) + 1

	for i in range(len(word2)):
		freq_2[word2[i]] = freq_2.get(word2[i], 0) + 1

	if freq == freq_2:
		return True
	else:
		return False


if __name__ == '__main__':

	word1 = 'tommarvoloriddle'  # Tom Marvolo Riddle
	word2 = 'iamlordvoldemort'  # I am Lord Voldemort

	word1 = 'test'  # Tom Marvolo Riddle
	word2 = 'estt'  # I am Lord Voldemort

	if isAnagram_1(word1, word2):
		print('Anagram')
	else:
		print('Not an Anagram')

	if isAnagram_2(word1, word2):
		print('Anagram')
	else:
		print('Not an Anagram')
