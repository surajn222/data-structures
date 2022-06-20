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


stack = Stack_list()
del stack