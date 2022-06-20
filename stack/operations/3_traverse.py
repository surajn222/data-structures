#create a stack of numbers
# create an empty stack with list
class Stack_list:
	def __init__(self):
		self.elements = []

	def push(self, data):
		self.elements.append(data)

	def pop(self):
		if self.elements:
			return self.elements.pop()
		else:
			return None

	def size(self):
		return len(self.elements)

	def empty(self):
		return True if self.size() == 0 else False

	def peek(self):
		return self.elements[-1]


stack = Stack_list()
print(stack.empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
stack.pop()
print(stack.peek())
# create an empty stack with deque


#access all values
#Not possible in stacks
# for index in range(len(stack_stack_name)):
#     print(stack_stack_name[index])


# accessing subarrays
# list from index one to index three
#Not possible in stacks
# stack_from_index_one_to_index_four = stack_stack_name[1:4] #Read as one to three
# print(stack_from_index_one_to_index_four)


# list from index one to index three
#Not possible in stacks
# stack_from_index_zero_to_index_four = stack_stack_name[:4] #Read as zero to three
# print(stack_from_index_zero_to_index_four)


# list from index one to index three
#Not possible in stacks
# stack_from_index_zero_to_index_last = stack_stack_name[-3:-1] #Read as zero to three
# print(stack_from_index_zero_to_index_last)
