# Define a class Linkedlist with variable head in constructor
class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def addNodesAtBegin(self, data):
        new_node = Node(data)

        # node1 should be assigned to new_node.next
        new_node.next = self.head

        # self.head should be assigned to new_node
        self.head = new_node





# Define a class node, with two variables in constructor, one input data and other next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Define a new Node
node1 = Node(data=1)

# Define a new Node
node2 = Node(data=2)


# Define a new Linkedlist
ll = LinkedList()

# Assign node1 to head
ll.head = node1

# Assign node2 to node1
ll.head.next = node2


# Add a traverse function in the linked list
ll.traverse()

# Add a add nodes function in the linkedlist
ll.addNodesAtBegin(0)

ll.traverse()