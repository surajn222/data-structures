# Step 1: List down all the subarrays first
# Step 2: In the inner loop, stop the subarray when the current_sum > target_sum
# Step 3:
# Step 4:
def findSublist1(array_1, target_sum):
	print(array_1)
	i = 0
	while i < len(array_1):
		j = 0
		while j < len(array_1):
			print("i = " + str(i) + ", j = " + str(j))
			j += 1
		i += 1


def findSublist2(array_1, target_sum):
	print(array_1)
	i = 0
	while i < len(array_1):
		j = i
		while j < len(array_1):
			print("i = " + str(i) + ", j = " + str(j))
			j += 1
		i += 1


def findSublist3(array_1, target_sum):
	print(array_1)
	i = 0
	while i < len(array_1):
		j = 0
		while j < len(array_1):
			if j > 3:
				break
			print("i = " + str(i) + ", j = " + str(j))
			j += 1
		i += 1


def findSublist4(array_1, target_sum):
	print(array_1)
	i = 0
	while i < len(array_1):
		j = i
		while j < len(array_1):
			if j > 3:
				break
			print("i = " + str(i) + ", j = " + str(j))
			j += 1
		i += 1


def findSublist5(array_1, target_sum):
	print(array_1)
	i = j = 0
	while i < len(array_1):
		while j < len(array_1):
			print("i = " + str(i) + ", j = " + str(j))
			j += 1
		i += 1


def findSublist6(array_1, target_sum):
	print(array_1)
	i = j = 0
	while i < len(array_1):
		while j < len(array_1):
			if j > 3:
				break
			print("i = " + str(i) + ", j = " + str(j))
			j += 1
		i += 1
		j = 2


def findSublist7(array_1, target_sum):
	print(array_1)
	i = j = 0
	while i < len(array_1):
		while j < len(array_1):
			if j > 3:
				break
			print("i = " + str(i) + ", j = " + str(j))
			j += 1
		i += 1
		j = 2


def findSublist8(array_1, target_sum):
	print(array_1)
	i = j = 0
	while i < len(array_1):
		while j < len(array_1):
			print("i = " + str(i) + ", j = " + str(j))
			print(array_1[i:j])
			j += 1
		i += 1
		print(array_1[i:j])
		j = 2


def findSublist9(array_1, target_sum):
	print(array_1)
	i = j = 0
	while i < len(array_1):
		while j < len(array_1):
			if j > 3:
				break
			print("i = " + str(i) + ", j = " + str(j))
			print(array_1[i:j + 1])
			j += 1
		i += 1
		print(array_1[i:j + 1])
		j = 2


def findSublist10(array_1, target_sum):
	print(array_1)
	i = j = 0
	while i < len(array_1):
		while j < len(array_1):
			if j > 3:
				break
			print("i = " + str(i) + ", j = " + str(j))
			print("Sum: " + str(sum(array_1[i:j + 1])))
			j += 1
		i += 1
		print("Sum: " + str(sum(array_1[i:j + 1])))
		j = 2


def findSublist11(array_1, target_sum):
	print(array_1)
	i = j = 0
	while i < len(array_1):
		while j < len(array_1):
			if j > 3:
				break
			print("i = " + str(i) + ", j = " + str(j))
			print("Sum: " + str(sum(array_1[i:j + 1])))
			current_sum = sum(array_1[i:j + 1])
			j += 1
		i += 1
		print("i = " + str(i) + ", j = " + str(j))
		print("Sum: " + str(sum(array_1[i:j + 1])))
		current_sum = sum(array_1[i:j + 1])
		j = 2


def findSublist12(array_1, target_sum):
	print(array_1)
	i = j = 0
	current_sum = 0
	while i < len(array_1):
		while j < len(array_1):
			if current_sum > target_sum:
				break
			print("i = " + str(i) + ", j = " + str(j))
			print("Sum: " + str(sum(array_1[i:j + 1])))
			current_sum = sum(array_1[i:j + 1])
			j += 1
		i += 1
		print("i = " + str(i) + ", j = " + str(j))
		print("Sum: " + str(sum(array_1[i:j + 1])))
		current_sum = sum(array_1[i:j + 1])
		j = 0


def findSublist13(array_1, target_sum):
	print(array_1)
	i = j = 0
	current_sum = 0
	while i < len(array_1):
		while j < len(array_1):
			if current_sum > target_sum:
				break
			print("i = " + str(i) + ", j = " + str(j) + ", Sum: " + str(sum(array_1[i:j + 1])))
			current_sum = sum(array_1[i:j + 1])
			j += 1
		i += 1
		print("i = " + str(i) + ", j = " + str(j) + ", Sum: " + str(sum(array_1[i:j + 1])))
		current_sum = sum(array_1[i:j + 1])


def findSublist14(array_1, target_sum):
	print(array_1)
	i = j = 0
	current_sum = array_1[0]
	count = 0
	while i < len(array_1):
		while j < len(array_1):
			print(
				"1 - i = " + str(i) + ", j = " + str(j) + ", Sum: " + str(current_sum) + " array: " + str(
					array_1[i:j + 1]))
			if current_sum == target_sum:
				print("Incrementing")
				count += 1

			if current_sum > target_sum:
				break

			j += 1
			if j < len(array_1):
				current_sum = current_sum + array_1[j]

		# current_sum = sum(array_1[i:j + 1])

		print("-------------")
		current_sum = current_sum - array_1[i]
		i += 1
		print(
			"2 - i = " + str(i) + ", j = " + str(j) + ", Sum: " + str(current_sum) + " array: " + str(array_1[i:j + 1]))

	print(count)


# j += 1


def subArraySum(arr, sum_):
	# Pick a starting point
	n = len(arr)
	for i in range(n):
		curr_sum = arr[i]

		# try all subarrays
		# starting with 'i'
		j = i + 1
		while j <= n:

			if curr_sum == sum_:
				print("Sum found between")
				print("indexes % d and % d" % (i, j - 1))

				return 1

			if curr_sum > sum_ or j == n:
				break

			curr_sum = curr_sum + arr[j]
			j += 1

	print("No subarray found")
	return 0


if __name__ == '__main__':
	# a list of positive integers
	nums = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
	nums = [1, 1, 1]
	nums = [1, 2, 3]
	# nums = [0, 9, 7, 2, 6, 1, 10, 3, 1, 4]
	# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	# target = 15
	target = 3

	# findSublist(nums, target)
	# findSublist1(nums, target)
	# findSublist2(nums, target)
	# findSublist3(nums, target)
	# findSublist4(nums, target)
	# findSublist5(nums, target)
	# findSublist6(nums, target)
	# findSublist7(nums, target)
	# findSublist8(nums, target)
	# findSublist9(nums, target)
	# findSublist10(nums, target)
	# findSublist11(nums, target)
	# findSublist12(nums, target)
	# findSublist13(nums, target)
	findSublist14(nums, target)
	subArraySum(nums, target)
