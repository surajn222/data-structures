# queue
from collections import deque


# Logic to generate binary numbers
# 0
# 1 -> 10 -> 100 .... # Add a 0 and 1 to every bit
#			 101
#	-> 11 -> 110 ... # Add a 0 and 1 to every number
# 		  -> 111

# Thus,
# Specific									# Generic
# 						push 1 to queue.
# Pull the 1, print it						# Pull the front element, print it
# Pull the 1, append 0, push to queue		# Pull the front element, append 0, push to queue
# Pull the 1, append 1, push to queue		# Pull the front element, append 1, push to queue
# Repeat above code and put it in for loop  # Repeat above code in a for loop


# Function to generate binary numbers between 1 and `n` using the
# queue data structure
def generate(n):
	# create an empty queue and enqueue 1
	q = deque()
	q.append('1')

	# run `n` times
	for i in range(n):
		# remove the front element
		front = str(q.popleft())
		print("Front: " + str(front))

		# append 0 and 1 to the front element of the queue and
		# enqueue both strings
		print("Appending: " + str(front + '0'))
		q.append(front + '0')
		print("Appending: " + str(front + '1'))
		q.append(front + '1')

		# print the front element
		print(front, end=' ')

	print("Final")
	print(str(q.popleft()))

if __name__ == '__main__':
	n = 16
	generate(n)
