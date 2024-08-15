# Recursive Python program for level
# order traversal of Binary Tree

# A node structure
class Node:
	# A utility function to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

# Function to print level order traversal of tree
def printLevelOrder(root):
	h = height(root)
	print("level")
	print("For root, level = 1")
	print("For level 2, i = 2")
	print("For level 3, i = 3")
	for i in range(1, h + 1):
		print("i = "+ str(i) + "")
		# i = level that we want printed, so recurse and reach that point
		printCurrentLevel(root, i)


# Print nodes at a current level
def printCurrentLevel(root, level):
	if root is None:
		return
	if level == 1:
		print(root.data, end="\n")
	elif level > 1:
		print("printcurrentlevel = " + str(level) + " data: " + str(root.data) + "")
		# Since we have not reached the desired level
		printCurrentLevel(root.left, level - 1)
		printCurrentLevel(root.right, level - 1)


""" Compute the height of a tree--the number of nodes
	along the longest path from the root node down to
	the farthest leaf node
"""


def height(node):
	if node is None:
		return 0
	else:
		# Compute the height of each subtree
		lheight = height(node.left)
		rheight = height(node.right)

		# Use the larger one
		if lheight > rheight:
			return lheight + 1
		else:
			return rheight + 1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
printLevelOrder(root)


# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


# --------------------------------------------------------------------

# Python program to print level
# order traversal using Queue

# A node structure


class Node:
	# A utility function to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


# Iterative Method to print the
# height of a binary tree


def printLevelOrder(root):
	# Base Case
	if root is None:
		return

	# Create an empty queue
	# for level order traversal
	queue = []

	# Enqueue Root and initialize height
	queue.append(root)

	while (len(queue) > 0):

		# Print front of queue and
		# remove it from queue
		print(queue[0].data)
		node = queue.pop(0)

		# Enqueue left child
		if node.left is not None:
			queue.append(node.left)

		# Enqueue right child
		if node.right is not None:
			queue.append(node.right)


# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
printLevelOrder(root)
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
