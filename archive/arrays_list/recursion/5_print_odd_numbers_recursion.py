def print_odd_numbers_recursion(i, max):
	if i < 10:
		if i % 2 == 1:
			print(i)
		i = i + 1
		print_odd_numbers_recursion(i, max)


max = 10
print_odd_numbers_recursion(0, max)
