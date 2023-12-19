# TODO: Completed
# Given an array where every element occurs three times, except one element which occurs only once. Find the element that occurs once. The expected time complexity is O(n) and O(1) extra space.
# Python3 code to find the element that
# appears once

# Logic:
# Given: Every element appears thrice, one elements appears once
# Lets first solve this for "Every element appears twice, one element appears once"
# Sol:
# Sum_twice = sum(all elements) * 2 = twice the array
# sum_array
# difference betn the above two, give you the element
# Eg. [2,2,5,5,7] = Sum_once = 2+2+5+5+7 = 21, sum_twice = (2+5+7)+(2+5+7) = 28 (contains one element twice)
# diff = 28-21 = 7

# Same goes for three
# [2,2,2,5,5,5,7]
# sum_once = 2+5+7 = 14
# sum_thrice = 2+5+7 + 2+5+7 + 2+5+7 = 42
# sum_array = 2+2+2+5+5+5+7
# diff = 42-29 = 14, divide by 2 (because 7 appears total of thrice, we subtracted twice), 14/2 = 7


def getSingle(arr, n):
	ones = 0
	twos = 0

	for i in range(n):
		# one & arr[i]" gives the bits that
		# are there in both 'ones' and new
		# element from arr[]. We add these
		# bits to 'twos' using bitwise XOR
		twos = twos ^ (ones & arr[i])

		# one & arr[i]" gives the bits that
		# are there in both 'ones' and new
		# element from arr[]. We add these
		# bits to 'twos' using bitwise XOR
		ones = ones ^ arr[i]

		# The common bits are those bits
		# which appear third time. So these
		# bits should not be there in both
		# 'ones' and 'twos'. common_bit_mask
		# contains all these bits as 0, so
		# that the bits can be removed from
		# 'ones' and 'twos'
		common_bit_mask = ~(ones & twos)

		# Remove common bits (the bits that
		# appear third time) from 'ones'
		ones &= common_bit_mask

		# Remove common bits (the bits that
		# appear third time) from 'twos'
		twos &= common_bit_mask
	return ones


# driver code
arr = [3, 3, 2, 3]
n = len(arr)
print("The element with single occurrence is ",
	  getSingle(arr, n))

# This code is contributed by "Abhishek Sharma 44"
