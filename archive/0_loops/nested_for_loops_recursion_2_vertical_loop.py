# Ever loop has the below three main parts
# 1. Init
# 2. End
# 3. Increment
# 4. Operation
# 5. Break, if required
j = 0
for i in range(5):
	j = j + i

	if i == 4:
		print(j)

# How to convert the same to recursion?

# Recursion is for loop on steroids. It has the same 4 parts

# Examples

# Nested Recursion
print("===============")


def print_recursion(i, lists, print_value):  # Init
	if i == len(lists):
		print("print_value: " + str(print_value))
		return

	i = i + 1
	for i in lists[i]:
		print_recursion(i, lists, print_value)


if __name__ == '__main__':
	i = 0
	lists = [
		["i1", "i2"]
	]
	print_value = ""
	print_recursion(i, lists, print_value)
