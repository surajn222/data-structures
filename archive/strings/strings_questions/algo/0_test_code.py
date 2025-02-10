# https://www.techiedelight.com/run-length-encoding-rle-data-compression-algorithm/
# Perform Run–length encoding (RLE) data compression algorithm on string `str`
def encode(s):
	encoding = ""  # stores output string

	i = 0
	while i < len(s):
		# count occurrences of character at index `i`
		# print(i)
		count = 1
		while i + 1 < len(s) and s[i] == s[i + 1]:
			count = count + 1
			i = i + 1
		print("count" + str(count) + ": " + str(s[i]))
		# print(s[i])
		i = i + 1


if __name__ == '__main__':
	s = 'ABBCCCD'  # Expected 1A2B3C1D
	print(encode(s))
