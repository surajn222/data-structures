# module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name

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


# stack = Stack_list()
# print(stack.empty())
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.peek())
# stack.pop()
# print(stack.peek())
# create an empty stack with deque
class Stack_deque:
	def __init__(self):
		from collections import deque
		self.elements = deque()

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

# stack_deque = Stack_deque()
# stack_deque.push(1)
# stack_deque.push(2)
# stack_deque.push(3)
# print(stack_deque.peek())
# stack_deque.pop()
# print(stack_deque.peek())


# Create stack from stack with queue module
class Stack_queue:
	def __init__(self):
		from queue import LifoQueue
		self.elements = LifoQueue(maxsize=3)

	def push(self, data):
		self.elements.put(data)

	def pop(self):
		if self.elements:
			return self.elements.get()
		else:
			return None

	def size(self):
		return self.elements.qsize()

	def empty(self):
		return True if self.size() == 0 else False

	def peek(self):
		return self.elements.queue[self.elements.qsize()-1]

stack_queue = Stack_queue()
stack_queue.push(1)
stack_queue.push(2)
stack_queue.push(3)
# print(stack_queue.size())
print(stack_queue.peek())
stack_queue.pop()
print(stack_queue.peek())


# create a stack of size
# create an empty stack with list
class Stack_list_with_size:
	def __init__(self, size):
		self.elements = []
		self.size = size

	def push(self, data):
		if len(self.elements) > self.size - 1:
			print("Stack full")
		else:
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


stack = Stack_list_with_size(2)
stack.push(1)
stack.push(2)
stack.push(3)
# print(stack.peek())
# stack.pop()
# print(stack.peek())

#Pending:
# deque stack with maxsize
# queue stack with maxsize

# create an empty stack with deque


# Cannot do a stack of the same elements

# create a stack of zeroes/ones/any character


# Cannot do a stack of the same elements
