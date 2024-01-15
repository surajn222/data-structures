import collections as col
import sys


# Insert some elements into the queue at first

# print('Dequeue: ' + str(my_deque))
# #insert x at right and B at left
# my_deque.append('x')
# my_deque.appendleft('B')

def maxSlidingWindow(nums, k):
	# if len(nums) == 1:
	# 	return nums
	#
	# if k == 1:
	# 	return nums

	i = 0
	j = 0
	list_window = []
	deque_max = col.deque('')
	list_return = []
	current_max = -1 * sys.maxsize

	while i <= len(nums) - k:
		print("--------------- array = " + str(nums))
		print("i = " + str(i))

		# If deque_max, first element is greater than nums[i], then append left. otherwise, remove the first element
		while j < k:
			print("j is less than k")
			if deque_max:
				while deque_max:
					if deque_max[0] < nums[j]:
						deque_max.popleft()
					else:
						break
				deque_max.appendleft(nums[j])

			else:
				deque_max.appendleft(nums[j])
			print(deque_max)
			j += 1

		print("j is greater than k")
		list_return.append(deque_max[-1])
		print("list return = " + str(list_return))
		if j < len(nums):
			while deque_max and deque_max[0] < nums[j]:
				deque_max.popleft()
			deque_max.appendleft(nums[j])

		# deque_max.appendleft(nums[i])
		print(deque_max)
		i += 1
		j += 1

	# print("after increment i = " + str(i) )

	# print("len nums - k = " + str(len(nums)-k))
	# print("i < len nums - k = " + str(i <= len(nums)-k))
	return list_return


# maxSlidingWindow([1,2,3,4,5, 6, 7, 8, 9], 3)
maxSlidingWindow([5, 3, 6, 1, 9, 2, 1, 10, 5], 3)
