from collections import deque


# Function to find duplicate parenthesis in an expression
def hasDuplicateParenthesis(exp):
	if not exp or len(exp) <= 3:
		return False

	# take an empty stack of characters
	stack = deque()

	# traverse the input expression
	for c in exp:
		# if the current char in the expression is not a closing parenthesis
		if c != ')':
			stack.append(c)
		# if the current char in the expression is a closing parenthesis
		else:
			# if the stack's top element is an opening parenthesis,
			# the subexpression of the form ((exp)) is found
			if stack[-1] == '(':
				return True

			# pop till '(' is found for current ')'
			while stack[-1] != '(':
				stack.pop()

			# pop '('
			stack.pop()

	# if we reach here, then the expression does not have any
	# duplicate parenthesis
	return False


if __name__ == '__main__':

	exp = '((x+y))'  # assumes valid expression

	if hasDuplicateParenthesis(exp):
		print('The expression has duplicate parenthesis.')
	else:
		print('The expression does not have duplicate parenthesis')
