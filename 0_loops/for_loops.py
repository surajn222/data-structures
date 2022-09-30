# Ever loop has the below three main parts
# 1. Init
# 2. End
# 3. Increment
# 4. Operation
# 5. Break, if required

for i in range(0, 10, 2):
	print(i)

# How to convert the same to recursion?

# Recursion is for loop on steroids. It has the same 4 parts

# Examples

# For loop
for i in range(0, 10, 2):
	print(i)

# Recursion

# Example 1
i = 0


def fun_print(i):  # Init
	print(i)  # Operation
	i = i + 1  # Increment
	if i == 10:  # End/Break
		return
	fun_print(i)  # Call the function again


fun_print(i)

print("Example 2")

# Example 1
i = 0


def fun_print(i):  # Init
	i = i + 1  # Increment
	if i < 10:
		fun_print(i)  # Call the function again #End
	print(i)


# Ways to stop calling a function:
# 1. Check a condition and not call a function
# 2. return statement

fun_print(i)
