# Function to find the longest common prefix between two strings
def LCP(X, Y):
	print("Comparing " + str(X) + " and " + str(Y))
	i = j = 0
	while i < len(X) and j < len(Y):
		if X[i] != Y[j]:
			break
		i = i + 1
		j = j + 1

	return X[:i]


# Function to find the longest common prefix (LCP) between a given set of strings
def findLCP(words):
	prefix = words[0]
	for s in words:
		prefix = LCP(prefix, s)
		print("Prefix is " + str(prefix))
	return prefix


if __name__ == '__main__':
	words = ['techie delight', 'tech', 'techie', 'technology', 'technical']
	print('The longest common prefix is', findLCP(words))

# Pseudo code:
# 1. Set a prefix (first word)
# 2. Find common letters between prefix and first word
# 3. Find common letters between prefix and second word
# 4. Find common letters between prefix and third word

# Takeaway
# Why this would work is because, the prefix which is common between the set of words, will only decrease
# We can use this mechanism to find other things like common letters in a set of words
# Anything common, we can do only one iteration
