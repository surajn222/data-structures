# Algo 1
def print_whole_numers_reverse_1(i, min):
	if i > min:
		print(i)
		i = i - 1
		print_whole_numers_reverse_1(i, min)


# Algo 2
def print_whole_numers_reverse_2(i, max):
	i = i + 1
	if i < max:
		print_whole_numers_reverse_2(i, max)
	print(i)
	return


i = 10
min = 0
# print_whole_numers_reverse_1(i, min)
max = 10
print_whole_numers_reverse_2(0, max)
