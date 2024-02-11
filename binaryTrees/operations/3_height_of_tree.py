class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def create_tree_4_height():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(4)
	root.left.left.left = Node(5)
	root.left.left.left.left = Node(6)
	return root

def create_tree_3_height():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	return root

def create_tree_2_height():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	return root

def create_tree_1_height():
	root = Node(1)
	return root

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

root = create_tree_1_height()
print("Height of tree is %d" % (height(root)))

root = create_tree_2_height()
print("Height of tree is %d" % (height(root)))

root = create_tree_3_height()
print("Height of tree is %d" % (height(root)))


print("Suraj explanation =============")

def height_step_1_iteration1(node):
	# Current height is the height of the tree so far, below the current one
	current_height = height_step_1_iteration2(node.left)
	# New height is the current level + 1
	new_height = current_height + 1
	return new_height

def height_step_1_iteration2(node):
	# Current height is the height of the tree so far, below the current one
	current_height = height_step_1_iteration3(node.left)
	# New height is the current level + 1
	new_height = current_height + 1
	return new_height

def height_step_1_iteration3(node):
	return 0

def height_step_1_iterationcombined(node):
	if node is None:
		return 0
	else:
		current_height = height_step_1_iterationcombined(node.left)
		# New height is the current level + 1
		new_height = current_height + 1
		return new_height


def height_step_1_iterationcombined_with_leftright(node):
	if node is None:
		return 0
	else:
		l_height = height_step_1_iterationcombined_with_leftright(node.left)
		r_height = height_step_1_iterationcombined_with_leftright(node.left)
		# New height is the current level + 1
		new_height = max(l_height, r_height) + 1
		return new_height

root = create_tree_1_height()
print("Height of 1 tree is %d" % (height_step_1_iterationcombined_with_leftright(root)))

root = create_tree_2_height()
print("Height of 2 tree is %d" % (height_step_1_iterationcombined_with_leftright(root)))

root = create_tree_3_height()
print("Height of 3 tree is %d" % (height_step_1_iterationcombined_with_leftright(root)))

root = create_tree_4_height()
print("Height of 4 tree is %d" % (height_step_1_iterationcombined_with_leftright(root)))
