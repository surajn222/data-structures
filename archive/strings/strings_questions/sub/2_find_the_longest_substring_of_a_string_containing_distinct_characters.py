# Function to find the longest substring with all
# distinct characters using a sliding window
def findLongestSubstring(s):
	# list to mark characters present in the current window
	window = {}

	# stores the longest substring boundaries
	begin = end = 0

	# `[low…high]` maintain the sliding window boundaries
	low = high = 0

	while high < len(s):

		# if the current character is present in the current window
		if window.get(s[high]):

			# remove characters from the left of the window till
			# we encounter the current character
			while s[low] != s[high]:
				window[s[low]] = False
				low = low + 1

			low = low + 1  # remove the current character
		else:
			# if the current character is not present in the current
			# window, include it
			window[s[high]] = True

			# update the maximum window size if necessary
			if end - begin < high - low:
				begin = low
				end = high

		high = high + 1

	# return the longest substring found at `s[begin…end]`
	return s[begin:end + 1]


if __name__ == '__main__':
	s = 'abbcdafeegh'
	print(findLongestSubstring(s))
