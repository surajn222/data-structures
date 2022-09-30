# Function to print all combinations of phrases that can be formed
# by words from each of the given lists
def printAllCombinations(lists, result='', n=0):  # Init
	# base case
	print("i = " + str(n))
	print("lists = " + str(lists))
	print("result = " + str(result))

	if not lists:  # End
		return

	# if we have traversed each list
	if n == len(lists):
		# print phrase after removing trailing space
		print("here i = " + str(n))
		print(result[1:])
		return  # End

	# do for each word in the current list

	for word in lists[n]:
		print("inside for loop")
		print("i = " + str(n))
		print("lists = " + str(lists[n]))
		out = result + " " + word  # append current word to output
		print("out = " + str(out))
		print("=========================================")

		printAllCombinations(lists, out, n + 1)  # recur for the next list


if __name__ == '__main__':
	lists = [
		["i1", "i2"],
		["j1", "j2", "j3"],
	]

	printAllCombinations(lists)
