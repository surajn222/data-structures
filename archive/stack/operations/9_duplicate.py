#create a stack of nubers
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

	def copy_object(self):
		return self.copy()

stack = Stack_list()
print(stack.empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
stack_2 = stack.copy_object()
print(stack_2)