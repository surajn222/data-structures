# Function to print sublist having a given sum using
# sliding window technique
def findSublist(nums, target):
	# maintains the sum of the current window
	windowSum = 0

	# maintain a window [low, high-1]
	(low, high) = (0, 0)

	# consider every sublist starting from `low` index
	for low in range(len(nums)):

		# if the current window's sum is less than the given sum,
		# then add elements to the current window from the right
		while windowSum < target and high < len(nums):
			windowSum += nums[high]
			high = high + 1

		# if the current window's sum is equal to the given sum
		if windowSum == target:
			print('Sublist found', (low, high - 1))
			return

		# At this point, the current window's sum is more than the given sum.
		# Remove the current element (leftmost element) from the window
		windowSum -= nums[low]


def findSublist2(array_1, target):
	print(array_1)

	i = j = 0
	window_sum = 0
	common_subarray = []
	while i <= len(array_1) - 1:

		while j < len(array_1):
			print("i = " + str(i) + ", j = " + str(j))
			window_sum = window_sum + array_1[j]
			common_subarray.append(array_1[j])
			print("Window: " + str(common_subarray))
			print("Window sum: " + str(window_sum))
			j += 1
			if window_sum > target:
				print("Breaking loop, incrementing i --------")
				print("--------")
				break

			print("--------")

		if i < len(array_1) - 1:
			i += 1
		print("Window2: " + str(common_subarray))
		common_subarray.pop(0)
		window_sum = window_sum - array_1[i]

	print("Window sum : " + str(window_sum))


if __name__ == '__main__':
	# a list of positive integers
	nums = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
	nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	target = 15

	# findSublist(nums, target)
	findSublist2(nums, target)
