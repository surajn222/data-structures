def print_odd_numbers_recursion(min, i):
	if i > 0:
		if i % 2 == 0:
			print(i)
		i = i - 1
		print_odd_numbers_recursion(min, i)


min = 10
print_odd_numbers_recursion(min, 10)
