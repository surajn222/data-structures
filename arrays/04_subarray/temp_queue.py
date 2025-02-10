import collections as col

# Insert some elements into the queue at first
my_deque = col.deque('')
print('Dequeue: ' + str(my_deque))
# insert x at right and B at left
my_deque.append('x')
my_deque.appendleft('B')
print('Dequeue after appending: ' + str(my_deque))

import collections as col


class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

		if len(nums) == 1 and k == 1:
			return nums

		i = 0
		j = 0
		# list_window = []
		deque_max = col.deque('')
		list_return = []
		# current_max = -1 * sys.maxsize
		deque_max.appendleft(nums[0])
		while i <= len(nums) - k:
			print("--------------- array = " + str(nums))
			print("i = " + str(i))

			# If deque_max, first element is greater than nums[i], then append left. otherwise, remove the first element
			while j < k:

				print("j is less than k = " + str(j) + " < " + str(k))

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

				if j == k - 1:
					print("j is, breaking " + str(j))
					break
				else:
					j += 1

			print("deque max before pop = " + str(deque_max))
			if deque_max:
				if nums[j] == deque_max[-1]:
					deque_max.pop()
			list_return.append(deque_max[-1])
			print("deque max after pop = " + str(deque_max))
			print("list return = " + str(list_return))

			i += 1
			j = + 1

			while deque_max and deque_max[0] < nums[j]:
				deque_max.popleft()
			deque_max.appendleft(nums[j])

		return list_return
