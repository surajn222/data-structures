def ngr(arr):
	stack = []
	for i in range(len(arr) - 1, -1, -1):
		print("arr index: " + str(arr[i]))
		# print(arr[i:])
		# print(stack)
		# Approach 1
		# for j in range(len(stack)-1, -1, -1):
		# 	print(stack[j])

		# Approach 2
		# count = len(stack)-1
		# while count > -1:
		# 	print(stack[count], end=", ")
		# 	count -= 1

		# Approach 3
		while stack and stack[-1] < arr[i]:
			stack.pop()

		print("After popping: " + str(stack))
		print("")
		stack.append(arr[i])


arr = [4, 6, 1, 8, 9, 3, 5]
ngr(arr)
