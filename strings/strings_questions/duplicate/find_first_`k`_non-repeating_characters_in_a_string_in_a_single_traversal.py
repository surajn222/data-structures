from heapq import heappop, heappush


class Pair:
	def __init__(self, count=0, index=0):
		self.count = count
		self.index = index

	# Override the `__lt__()` function to make `Pair` class work with min-heap
	def __lt__(self, other):
		return self.count < other.count


# Function to find first `k` non-repeating character in
# the string by doing only a single traversal
def first_k_non_repeating(s, k):
	# dictionary to store character count and the index of its
	# last occurrence in the string
	d = {}

	for i in range(len(s)):
		pair = d.setdefault(s[i], Pair())
		pair.count = pair.count + 1
		pair.index = i

	# create an empty min-heap
	pq = []

	# traverse the dictionary and push the index of all characters
	# having the count of 1 into the min-heap
	for pair in d.values():
		if pair.count == 1:
			heappush(pq, pair.index)

	# pop the top `k` keys from the min-heap
	while k > 0 and pq:
		# extract the minimum node from the min-heap
		print(s[heappop(pq)], end=' ')
		k = k - 1


if __name__ == '__main__':
	s = 'ABCDBAGHCHFAC'
	k = 3

	first_k_non_repeating(s, k)
