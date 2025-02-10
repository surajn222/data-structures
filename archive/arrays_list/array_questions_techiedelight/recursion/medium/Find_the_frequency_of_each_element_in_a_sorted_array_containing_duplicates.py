# Function to find the frequency of each element in a sorted list
def findFrequency(nums, left, right, freq):
	if left > right:
		return

	# if every element in sublist nums[left…right] is equal,
	# then increment the element's count by `n`
	if nums[left] == nums[right]:

		count = freq.get(nums[left])
		if count is None:
			count = 0

		freq[nums[left]] = count + (right - left + 1)
		return

	mid = (left + right) // 2

	# divide the list into left and right sublist and recur
	findFrequency(nums, left, mid, freq)
	findFrequency(nums, mid + 1, right, freq)


if __name__ == '__main__':
	nums = [2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9]

	# find the frequency of each element in the list and store it in a dictionary
	freq = {}
	findFrequency(nums, 0, len(nums) - 1, freq)
	print(freq)
