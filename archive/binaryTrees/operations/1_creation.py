# First, create a class Node, with three variables, left, right and value
class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

if __name__ == '__main__':
	# Create this tree:
	'''
			1	
		2		 3
	4 
	'''

	# Create root Node
	root = Node(1)
	''' following is the tree after above statement
		1
		/ \
	None None
	'''

	# Set root left and right nodes
	root.left = Node(2)
	root.right = Node(3)
	''' 2 and 3 become left and right children of 1
		1
		/ \
		2	 3
		/ \ / \
	None None None None'''

	# Set root left child's left node
	root.left.left = Node(4)
	'''4 becomes left child of 2
			1	
		2		 3
	4 
	'''