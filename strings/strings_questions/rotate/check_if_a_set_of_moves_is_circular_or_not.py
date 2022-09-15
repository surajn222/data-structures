# Function to check if the given set of moves is circular or not
def isCircularMove(s):
	# start from coordinates (0, 0)
	x = y = 0

	# assume that the initial direction is North
	dir = 'N'

	# read each instruction from the input string
	for c in s:
		# move one unit in the same direction
		if c == 'M':
			if dir == 'N':
				y = y + 1
			elif dir == 'S':
				y = y - 1
			elif dir == 'E':
				x = x + 1
			elif dir == 'W':
				x = x - 1

		# change direction to the left of the current direction
		if c == 'L':
			if dir == 'N':
				dir = 'W'
			elif dir == 'W':
				dir = 'S'
			elif dir == 'S':
				dir = 'E'
			elif dir == 'E':
				dir = 'N'

		# change direction to the right of the current direction
		if c == 'R':
			if dir == 'N':
				dir = 'E'
			elif dir == 'E':
				dir = 'S'
			elif dir == 'S':
				dir = 'W'
			elif dir == 'W':
				dir = 'N'

	# if we are back to starting coordinates (0, 0),
	# the move is circular
	return x == 0 and y == 0


if __name__ == '__main__':

	s = 'MMRMMRMMRMM'

	if isCircularMove(s):
		print('Circular move')
	else:
		print('Non-circular move')
