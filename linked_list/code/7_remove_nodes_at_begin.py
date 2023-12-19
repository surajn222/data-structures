# Define a LinkedList class
class Linkedlist:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next # If this is None, while loop will not run again

    def removeNodesAtBegin(self):
        # Assign the second node, head.next to head
        self.head = self.head.next

# Define a class Node with two variables, data and next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Define a new node
node1 = Node(data=1)

# Define another new node
node2 = Node(data=2)


# Define a Linkedlist object
ll = Linkedlist()

# Assign nodes to Linkedlist
ll.head = node1
ll.head.next = node2

# Define a traverse function
ll.traverse()

ll.removeNodesAtBegin()

ll.traverse()