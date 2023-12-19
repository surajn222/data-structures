
# Define LinkedList(head)
class LinkedList:
    def __int__(self):
        self.head = None

    def traverse(self):
        # Assign head to a temp variable
        temp = self.head

        # While temp is not None, print the data, get next of temp and assign it to temp
        while(temp):
            print(temp.data)
            temp = temp.next

# Node(data = input, next = None)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# node1 = Node(data=1, next=None)
node1 = Node(data=1)

# Linkedlist(head)
ll = LinkedList()
ll.head = node1

ll.traverse()