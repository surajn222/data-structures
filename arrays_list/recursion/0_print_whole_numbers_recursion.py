def print_whole_numbers(i, max):
	if i < max:
		print(i)
		i += 1
		print_whole_numbers(i, max)
	return


i = 0
print_whole_numbers(i, 10)
