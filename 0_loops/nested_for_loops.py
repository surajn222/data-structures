# Ever loop has the below three main parts
# 1. Init
# 2. End
# 3. Increment
# 4. Operation
# 5. Break, if required

for i in range(4):
	print("i:" + str(i))
	for j in range(4):
		print("\tj:" + str(j))

for i in range(4):
	print("i:" + str(i))
	for j in range(4):
		print("\tj:" + str(j))
		for k in range(4):
			print("\t\tk:" + str(k))


# How to convert the same to recursion?

# Recursion is for loop on steroids. It has the same 4 parts

# Examples

# Nested Recursion

def print_recursion(lists, result='', n=0):  # Init
	# base case
	if not lists:  # End
		return

	# if we have traversed each list
	# Final result
	if n == len(lists):
		# print phrase after removing trailing space
		print("here i = " + str(n))
		print(result[1:])
		return  # End

	# do for each word in the current list
	# Recursion call
	for word in lists[n]:
		final_result = result + " " + word  # append current word to output
		print("out = " + str(final_result))
		print("=========================================")

		print_recursion(lists, final_result, n + 1)  # recur for the next list


if __name__ == '__main__':
	lists = [
		["i1", "i2"],
		["j1", "j2", "j3"],
	]

	print_recursion(lists)
