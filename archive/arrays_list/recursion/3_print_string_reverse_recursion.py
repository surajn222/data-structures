def print_string_reverse_recursion(str1):
	i = 0

	if i < len(str1) - 1:
		i = i + 1
		print_string_reverse_recursion(str1[i:])
	print(str1[i - 1])


str1 = "STRING1"
print_string_reverse_recursion(str1)

# There are other better ways online
